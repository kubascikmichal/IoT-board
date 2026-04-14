from machine import Pin, I2C
import ssd1306

SDA_PIN = 1
SCL_PIN = 2

WIDTH = 128
HEIGHT = 64

i2c = I2C(0, sda=Pin(SDA_PIN), scl=Pin(SCL_PIN), freq=400000)
oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)


def show_lines(lines: list[str]) -> None:
    oled.fill(0)
    for i, line in enumerate(lines[:6]):
        oled.text(line[:21], 0, i * 10)
    oled.show()


show_lines(["IoT Stich board", "SSD1306 ready"]) 
print("Zadaj text na displej. Pre koniec napis 'exit'.")

while True:
    text = input("> ").strip()
    if text.lower() == "exit":
        show_lines(["Koniec programu"]) 
        break

    show_lines(["Text:", text])
