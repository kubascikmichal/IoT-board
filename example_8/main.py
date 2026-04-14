from machine import Pin
import dht
import time

DHT_PIN = 18

sensor = dht.DHT22(Pin(DHT_PIN))

print("DHT meranie spustene")
print("Stlac Ctrl+C pre koniec")

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("Teplota:", temp, "C | Vlhkost:", hum, "%")
    except OSError:
        print("Chyba citania zo senzora DHT")

    time.sleep(2)
