from machine import Pin, PWM, I2C, ADC
import time

# Pin mapping podla schemy
PIN_I2C_SDA = 1
PIN_I2C_SCL = 2
PIN_RGB_B = 3
PIN_LED_DATA = 4
PIN_RGB_G = 5
PIN_RGB_R = 7
PIN_BUZZER = 11
PIN_PHOTO = 16
PIN_DHT = 18
PIN_BTN_4 = 33
PIN_BTN_3 = 35
PIN_BTN_2 = 37
PIN_BTN_1 = 39

WS2812_COUNT = 12

results = []


def add_result(name, ok, note=""):
    state = "PASS" if ok else "FAIL"
    results.append((name, state, note))
    print("[%s] %s %s" % (state, name, note))


def ask_yes_no(question):
    while True:
        ans = input(question + " [y/n]: ").strip().lower()
        if ans in ("y", "yes", "a", "ano"):
            return True
        if ans in ("n", "no", "nie"):
            return False
        print("Zadaj y alebo n.")


def test_oled():
    try:
        import ssd1306

        i2c = I2C(0, sda=Pin(PIN_I2C_SDA), scl=Pin(PIN_I2C_SCL), freq=400000)
        oled = ssd1306.SSD1306_I2C(128, 64, i2c)
        oled.fill(0)
        oled.text("IoT Stich board", 0, 0)
        oled.text("SELF TEST", 0, 12)
        oled.text("Skus poklep DPS", 0, 24)
        oled.text("a sleduj vypadky", 0, 36)
        oled.show()
        ok = ask_yes_no("Vidis text na OLED?")
        add_result("OLED", ok)
    except Exception as e:
        add_result("OLED", False, "(chyba: %s)" % str(e))


def test_rgb_discrete():
    try:
        r = Pin(PIN_RGB_R, Pin.OUT)
        g = Pin(PIN_RGB_G, Pin.OUT)
        b = Pin(PIN_RGB_B, Pin.OUT)

        sequence = [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1),
            (1, 1, 1),
            (0, 0, 0),
        ]

        for rv, gv, bv in sequence:
            r.value(rv)
            g.value(gv)
            b.value(bv)
            time.sleep_ms(300)

        ok = ask_yes_no("RGB LED menila farby stabilne?")
        add_result("RGB LED (bez PWM)", ok)
    except Exception as e:
        add_result("RGB LED (bez PWM)", False, "(chyba: %s)" % str(e))


def test_ws2812():
    try:
        import neopixel

        np = neopixel.NeoPixel(Pin(PIN_LED_DATA), WS2812_COUNT)
        colors = [
            (255, 0, 0),
            (0, 255, 0),
            (0, 0, 255),
            (255, 255, 255),
            (0, 0, 0),
        ]

        for color in colors:
            for i in range(WS2812_COUNT):
                np[i] = color
            np.write()
            time.sleep_ms(300)

        ok = ask_yes_no("Seriove RGB LED svietili bez vypadkov?")
        add_result("WS2812 LED", ok)
    except Exception as e:
        add_result("WS2812 LED", False, "(chyba: %s)" % str(e))


def test_buzzer():
    try:
        bz = PWM(Pin(PIN_BUZZER), freq=1000, duty=0)
        for f in (523, 659, 784):
            bz.freq(f)
            bz.duty(512)
            time.sleep_ms(180)
            bz.duty(0)
            time.sleep_ms(60)

        ok = ask_yes_no("Pocul si tri tony na bzuciaku?")
        add_result("Bzuciak PWM", ok)
    except Exception as e:
        add_result("Bzuciak PWM", False, "(chyba: %s)" % str(e))


def test_buttons():
    try:
        buttons = [
            ("USR1", Pin(PIN_BTN_1, Pin.IN)),
            ("USR2", Pin(PIN_BTN_2, Pin.IN)),
            ("USR3", Pin(PIN_BTN_3, Pin.IN)),
            ("USR4", Pin(PIN_BTN_4, Pin.IN)),
        ]

        all_ok = True
        for name, btn in buttons:
            print("Stlac %s do 5 sekund..." % name)
            pressed = False
            start = time.ticks_ms()
            while time.ticks_diff(time.ticks_ms(), start) < 5000:
                if btn.value() == 0:
                    pressed = True
                    while btn.value() == 0:
                        time.sleep_ms(20)
                    break
                time.sleep_ms(20)

            if not pressed:
                all_ok = False
                print("%s nebolo stlacene alebo nereaguje." % name)

        add_result("Tlacidla USR1-4", all_ok)
    except Exception as e:
        add_result("Tlacidla USR1-4", False, "(chyba: %s)" % str(e))


def test_photo():
    try:
        adc = ADC(Pin(PIN_PHOTO))
        try:
            adc.atten(ADC.ATTN_11DB)
        except AttributeError:
            pass

        min_v = 65535
        max_v = 0

        print("Zakry a odkry fotorezistor (3 sekundy)...")
        start = time.ticks_ms()
        while time.ticks_diff(time.ticks_ms(), start) < 3000:
            v = adc.read()
            if v < min_v:
                min_v = v
            if v > max_v:
                max_v = v
            time.sleep_ms(25)

        span = max_v - min_v
        ok = span > 150
        add_result("Fotorezistor", ok, "(min=%d max=%d)" % (min_v, max_v))
    except Exception as e:
        add_result("Fotorezistor", False, "(chyba: %s)" % str(e))


def test_dht():
    try:
        import dht

        sensor = None
        try:
            sensor = dht.DHT22(Pin(PIN_DHT))
            sensor.measure()
        except Exception:
            sensor = dht.DHT11(Pin(PIN_DHT))
            sensor.measure()

        t = sensor.temperature()
        h = sensor.humidity()
        ok = (t is not None) and (h is not None)
        add_result("DHT", ok, "(T=%sC H=%s%%)" % (str(t), str(h)))
    except Exception as e:
        add_result("DHT", False, "(chyba: %s)" % str(e))


print("\n=== TEST DOSKY IoT Stich board ===")
print("Tip: pocas testu jemne poklep na DPS na odhalenie studenych spojov.")

# Testy
for fn in (
    test_oled,
    test_rgb_discrete,
    test_ws2812,
    test_buzzer,
    test_buttons,
    test_photo,
    test_dht,
):
    print("\n---")
    fn()

print("\n=== SUMAR ===")
pass_count = 0
for name, state, note in results:
    print("%s: %s %s" % (name, state, note))
    if state == "PASS":
        pass_count += 1

print("\nPASS: %d / %d" % (pass_count, len(results)))
if pass_count == len(results):
    print("Doska presla testom.")
else:
    print("Niektore casti zlyhali. Skontroluj zapojenie, napajanie a spoje.")
