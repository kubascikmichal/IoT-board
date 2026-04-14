from machine import Pin
import neopixel
import time

LED_PIN = 4
LED_COUNT = 12

np = neopixel.NeoPixel(Pin(LED_PIN), LED_COUNT)


def fill_color(r: int, g: int, b: int) -> None:
    for i in range(LED_COUNT):
        np[i] = (r, g, b)
    np.write()


def rainbow_step(delay_ms: int = 120) -> None:
    colors = [
        (255, 0, 0),
        (255, 80, 0),
        (255, 255, 0),
        (0, 255, 0),
        (0, 0, 255),
        (120, 0, 255),
    ]
    for color in colors:
        fill_color(*color)
        time.sleep_ms(delay_ms)


print("WS2812 ovladanie")
print("Prikazy: red, green, blue, white, off, rainbow, exit")

while True:
    cmd = input("> ").strip().lower()

    if cmd == "red":
        fill_color(255, 0, 0)
    elif cmd == "green":
        fill_color(0, 255, 0)
    elif cmd == "blue":
        fill_color(0, 0, 255)
    elif cmd == "white":
        fill_color(255, 255, 255)
    elif cmd == "off":
        fill_color(0, 0, 0)
    elif cmd == "rainbow":
        rainbow_step()
    elif cmd == "exit":
        fill_color(0, 0, 0)
        break
    else:
        print("Neznamy prikaz")
