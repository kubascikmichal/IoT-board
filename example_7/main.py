from machine import Pin, ADC
import time

PHOTO_PIN = 16
SAMPLE_COUNT = 100

adc = ADC(Pin(PHOTO_PIN))
try:
    adc.atten(ADC.ATTN_11DB)
except AttributeError:
    pass


def normalize(value: int, min_v: int, max_v: int) -> int:
    if max_v <= min_v:
        return 0
    return int((value - min_v) * 100 / (max_v - min_v))


print("Kalibracia fotorezistora...")
min_val = 65535
max_val = 0

for _ in range(SAMPLE_COUNT):
    val = adc.read()
    if val < min_val:
        min_val = val
    if val > max_val:
        max_val = val
    time.sleep_ms(20)

print("Kalibracia hotova")
print("MIN:", min_val, "MAX:", max_val)
print("Stlac Ctrl+C pre koniec")

while True:
    value = adc.read()
    percent = normalize(value, min_val, max_val)
    print("RAW:", value, "LIGHT[%]:", percent)
    time.sleep_ms(500)
