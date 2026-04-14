from machine import Pin

R_PIN = 7
G_PIN = 5
B_PIN = 3

red = Pin(R_PIN, Pin.OUT)
green = Pin(G_PIN, Pin.OUT)
blue = Pin(B_PIN, Pin.OUT)


def set_rgb(r: int, g: int, b: int) -> None:
    red.value(1 if r else 0)
    green.value(1 if g else 0)
    blue.value(1 if b else 0)


def all_off() -> None:
    set_rgb(0, 0, 0)


print("RGB bez PWM")
print("Prikazy: red, green, blue, yellow, cyan, magenta, white, off, exit")

while True:
    cmd = input("> ").strip().lower()

    if cmd == "red":
        set_rgb(1, 0, 0)
    elif cmd == "green":
        set_rgb(0, 1, 0)
    elif cmd == "blue":
        set_rgb(0, 0, 1)
    elif cmd == "yellow":
        set_rgb(1, 1, 0)
    elif cmd == "cyan":
        set_rgb(0, 1, 1)
    elif cmd == "magenta":
        set_rgb(1, 0, 1)
    elif cmd == "white":
        set_rgb(1, 1, 1)
    elif cmd == "off":
        all_off()
    elif cmd == "exit":
        all_off()
        break
    else:
        print("Neznamy prikaz")
