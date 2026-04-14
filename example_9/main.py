import socket
import time
import network
from machine import Pin, PWM, I2C

try:
    import dht
except ImportError:
    dht = None

try:
    import neopixel
except ImportError:
    neopixel = None

try:
    import ssd1306
except ImportError:
    ssd1306 = None

# Pin mapping
PIN_DHT = 18
PIN_WS = 4
PIN_R = 7
PIN_G = 5
PIN_B = 3
PIN_BUZZER = 11
PIN_SDA = 1
PIN_SCL = 2

WS_COUNT = 12
AP_SSID = "IoTStich-AP"
AP_PASSWORD = "iotstich123"

# Peripherals
red = Pin(PIN_R, Pin.OUT)
green = Pin(PIN_G, Pin.OUT)
blue = Pin(PIN_B, Pin.OUT)
buzzer = PWM(Pin(PIN_BUZZER), freq=1000, duty=0)

sensor = dht.DHT22(Pin(PIN_DHT)) if dht else None
np = neopixel.NeoPixel(Pin(PIN_WS), WS_COUNT) if neopixel else None

oled = None
if ssd1306:
    try:
        i2c = I2C(0, sda=Pin(PIN_SDA), scl=Pin(PIN_SCL), freq=400000)
        oled = ssd1306.SSD1306_I2C(128, 64, i2c)
    except Exception:
        oled = None


def set_rgb(name):
    colors = {
        "off": (0, 0, 0),
        "red": (1, 0, 0),
        "green": (0, 1, 0),
        "blue": (0, 0, 1),
        "white": (1, 1, 1),
        "yellow": (1, 1, 0),
        "cyan": (0, 1, 1),
        "magenta": (1, 0, 1),
    }
    r, g, b = colors.get(name, (0, 0, 0))
    red.value(r)
    green.value(g)
    blue.value(b)


def set_ws(name):
    if np is None:
        return
    colors = {
        "off": (0, 0, 0),
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "white": (255, 255, 255),
        "yellow": (255, 255, 0),
        "cyan": (0, 255, 255),
        "magenta": (255, 0, 255),
    }
    color = colors.get(name, (0, 0, 0))
    for i in range(WS_COUNT):
        np[i] = color
    np.write()


def buzz(ms=200, freq=1200):
    buzzer.freq(freq)
    buzzer.duty(512)
    time.sleep_ms(ms)
    buzzer.duty(0)


def read_dht():
    if sensor is None:
        return None, None
    try:
        sensor.measure()
        return sensor.temperature(), sensor.humidity()
    except Exception:
        return None, None


def oled_text(line1, line2=""):
    if oled is None:
        return
    oled.fill(0)
    oled.text("IoT Stich AP", 0, 0)
    oled.text(line1[:21], 0, 16)
    oled.text(line2[:21], 0, 28)
    oled.show()


def parse_query(path):
    out = {}
    if "?" not in path:
        return out
    query = path.split("?", 1)[1]
    if " " in query:
        query = query.split(" ", 1)[0]
    for pair in query.split("&"):
        if "=" in pair:
            k, v = pair.split("=", 1)
            out[k] = v
    return out


def html_page(temp, hum):
    t = "-" if temp is None else "%.1f" % temp
    h = "-" if hum is None else "%.1f" % hum
    return """<!doctype html>
<html>
<head>
<meta charset=\"utf-8\">
<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">
<title>IoT Stich AP</title>
<style>
body{font-family:Arial,sans-serif;margin:20px;background:#f3f6fa}
.card{background:#fff;border-radius:12px;padding:16px;margin-bottom:12px;box-shadow:0 2px 8px rgba(0,0,0,.08)}
a.btn{display:inline-block;padding:8px 12px;margin:4px;background:#0b67ff;color:#fff;text-decoration:none;border-radius:8px}
a.alt{background:#444}
</style>
</head>
<body>
<div class=\"card\"><h2>IoT Stich board</h2><p>DHT teplota: <b>""" + t + """ C</b><br>DHT vlhkost: <b>""" + h + """ %</b></p><a class=\"btn\" href=\"/\">Obnovit</a></div>
<div class=\"card\"><h3>RGB LED</h3>
<a class=\"btn\" href=\"/?rgb=red\">Red</a><a class=\"btn\" href=\"/?rgb=green\">Green</a><a class=\"btn\" href=\"/?rgb=blue\">Blue</a><a class=\"btn\" href=\"/?rgb=white\">White</a><a class=\"btn alt\" href=\"/?rgb=off\">Off</a></div>
<div class=\"card\"><h3>WS2812</h3>
<a class=\"btn\" href=\"/?ws=red\">Red</a><a class=\"btn\" href=\"/?ws=green\">Green</a><a class=\"btn\" href=\"/?ws=blue\">Blue</a><a class=\"btn\" href=\"/?ws=white\">White</a><a class=\"btn alt\" href=\"/?ws=off\">Off</a></div>
<div class=\"card\"><h3>Bzuciak</h3>
<a class=\"btn\" href=\"/?buzz=1\">Pipni</a></div>
<div class=\"card\"><h3>OLED</h3>
<a class=\"btn\" href=\"/?oled=hello\">Hello</a><a class=\"btn\" href=\"/?oled=dht\">DHT</a><a class=\"btn alt\" href=\"/?oled=clear\">Clear</a></div>
</body></html>"""


def start_ap():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=AP_SSID, password=AP_PASSWORD, authmode=3)
    while not ap.active():
        time.sleep_ms(100)
    print("AP SSID:", AP_SSID)
    print("AP IP:", ap.ifconfig()[0])


def run_server():
    addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(2)
    print("HTTP server bezi na 192.168.4.1")

    oled_text("AP: " + AP_SSID, "IP: 192.168.4.1")

    while True:
        conn, _ = s.accept()
        req = conn.recv(1024)
        path = "/"
        try:
            line = req.decode().split("\r\n")[0]
            path = line.split(" ")[1]
        except Exception:
            pass

        q = parse_query(path)
        if "rgb" in q:
            set_rgb(q["rgb"])
        if "ws" in q:
            set_ws(q["ws"])
        if q.get("buzz") == "1":
            buzz()
        if "oled" in q:
            if q["oled"] == "hello":
                oled_text("Ahoj student!", "OLED funguje")
            elif q["oled"] == "dht":
                t, h = read_dht()
                oled_text("T=%s C" % ("-" if t is None else "%.1f" % t), "H=%s %%" % ("-" if h is None else "%.1f" % h))
            elif q["oled"] == "clear" and oled is not None:
                oled.fill(0)
                oled.show()

        t, h = read_dht()
        html = html_page(t, h)
        conn.send("HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nConnection: close\r\n\r\n")
        conn.send(html)
        conn.close()


start_ap()
run_server()
