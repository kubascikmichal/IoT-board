from machine import Pin, I2C
import ssd1306
import time

SDA_PIN = 1
SCL_PIN = 2

BTN_PINS = [39, 37, 35, 33]
BTN_NAMES = ["USR1", "USR2", "USR3", "USR4"]
DEBOUNCE_MS = 60

WIDTH = 128
HEIGHT = 64

i2c = I2C(0, sda=Pin(SDA_PIN), scl=Pin(SCL_PIN), freq=400000)
oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

press_started = [False, False, False, False]
press_start_ms = [0, 0, 0, 0]
last_edge_ms = [0, 0, 0, 0]
press_duration_ms = [0, 0, 0, 0]
pending_event = [False, False, False, False]


def show_lines(lines):
    oled.fill(0)
    for i, line in enumerate(lines[:6]):
        oled.text(line[:21], 0, i * 10)
    oled.show()


def make_irq_handler(idx):
    def handler(pin):
        now = time.ticks_ms()

        # Debounce delay: hrany, ktore pridu skor ako DEBOUNCE_MS, ignorujeme.
        if time.ticks_diff(now, last_edge_ms[idx]) < DEBOUNCE_MS:
            return

        last_edge_ms[idx] = now

        if pin.value() == 0:
            press_started[idx] = True
            press_start_ms[idx] = now
        elif press_started[idx]:
            press_started[idx] = False
            press_duration_ms[idx] = time.ticks_diff(now, press_start_ms[idx])
            pending_event[idx] = True

    return handler


buttons = []
handlers = []
for i, gpio in enumerate(BTN_PINS):
    btn = Pin(gpio, Pin.IN, Pin.PULL_UP)
    irq_handler = make_irq_handler(i)
    btn.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=irq_handler)
    buttons.append(btn)
    handlers.append(irq_handler)


show_lines(["IoT Stich board", "Test tlacidiel IRQ", "Stlac USR1-USR4"])
print("Meranie dlzky stlacenia tlacidiel USR1-USR4")
print("Debounce delay: %d ms" % DEBOUNCE_MS)
print("Stlac Ctrl+C pre koniec")

while True:
    for i, is_pending in enumerate(pending_event):
        if is_pending:
            pending_event[i] = False
            duration = press_duration_ms[i]
            msg = "%s: %d ms" % (BTN_NAMES[i], duration)
            print(msg)
            show_lines([
                "Prerusenie tlacidla",
                BTN_NAMES[i],
                "Dlzka: %d ms" % duration,
                "Debounce: %d ms" % DEBOUNCE_MS,
            ])

    time.sleep_ms(20)
