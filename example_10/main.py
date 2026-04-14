import network
import socket
import time
from machine import Pin

try:
    import dht
except ImportError:
    dht = None

WIFI_SSID = "TVOJA_WIFI"
WIFI_PASSWORD = "TVOJE_HESLO"
THINGSPEAK_API_KEY = "TVOJ_WRITE_API_KEY"

DHT_PIN = 18
SEND_INTERVAL_SEC = 20

sensor = dht.DHT22(Pin(DHT_PIN)) if dht else None


def wifi_connect(ssid, password, timeout_sec=15):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if wlan.isconnected():
        return wlan

    print("Pripajam sa na Wi-Fi:", ssid)
    wlan.connect(ssid, password)

    start = time.time()
    while not wlan.isconnected() and (time.time() - start) < timeout_sec:
        time.sleep(1)
        print(".", end="")
    print()

    if not wlan.isconnected():
        raise RuntimeError("Wi-Fi pripojenie zlyhalo")

    print("Wi-Fi OK, IP:", wlan.ifconfig()[0])
    return wlan


def read_dht():
    if sensor is None:
        return None, None
    try:
        sensor.measure()
        return sensor.temperature(), sensor.humidity()
    except Exception:
        return None, None


def thingspeak_update(api_key, temp, hum):
    host = "api.thingspeak.com"
    path = "/update?api_key={}&field1={}&field2={}".format(api_key, temp, hum)
    addr = socket.getaddrinfo(host, 80)[0][-1]

    s = socket.socket()
    s.connect(addr)
    req = "GET {} HTTP/1.1\r\nHost: {}\r\nConnection: close\r\n\r\n".format(path, host)
    s.send(req.encode())

    response = s.recv(512)
    s.close()
    return response


def main():
    if THINGSPEAK_API_KEY == "TVOJ_WRITE_API_KEY":
        raise RuntimeError("Dopln THINGSPEAK_API_KEY v main.py")

    wifi_connect(WIFI_SSID, WIFI_PASSWORD)

    while True:
        t, h = read_dht()
        if t is None or h is None:
            print("DHT chyba, skusam znovu...")
        else:
            print("T=%.1f C, H=%.1f %%" % (t, h))
            resp = thingspeak_update(THINGSPEAK_API_KEY, t, h)
            ok = b" 200 " in resp or b"\n0\n" not in resp
            print("ThingSpeak odoslanie:", "OK" if ok else "CHECK")

        time.sleep(SEND_INTERVAL_SEC)


main()
