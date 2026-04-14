from machine import Pin, PWM

R_PIN = 7
G_PIN = 5
B_PIN = 3

red = PWM(Pin(R_PIN), freq=1000, duty=0)
green = PWM(Pin(G_PIN), freq=1000, duty=0)
blue = PWM(Pin(B_PIN), freq=1000, duty=0)


def clamp(value: int) -> int:
    return max(0, min(1023, value))


def set_rgb(r: int, g: int, b: int) -> None:
    red.duty(clamp(r))
    green.duty(clamp(g))
    blue.duty(clamp(b))


print("RGB s PWM")
print("Zadaj tri hodnoty oddelene medzerou: R G B (0-1023)")
print("Priklad: 1023 0 0")
print("Pre koniec napis: exit")

while True:
    raw = input("> ").strip().lower()

    if raw == "exit":
        set_rgb(0, 0, 0)
        break

    parts = raw.split()
    if len(parts) != 3:
        print("Zadaj presne 3 cisla.")
        continue

    try:
        r, g, b = [int(x) for x in parts]
    except ValueError:
        print("Vsetky hodnoty musia byt cisla.")
        continue

    set_rgb(r, g, b)
