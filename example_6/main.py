from machine import Pin, PWM
import time

BUZZER_PIN = 11

buzzer = PWM(Pin(BUZZER_PIN), freq=1000, duty=0)


def beep(freq: int, duration_ms: int = 200, duty: int = 512) -> None:
    buzzer.freq(max(50, freq))
    buzzer.duty(max(0, min(1023, duty)))
    time.sleep_ms(duration_ms)
    buzzer.duty(0)


def play_melody() -> None:
    melody = [523, 659, 784, 659, 523, 392]
    for note in melody:
        beep(note, 180)
        time.sleep_ms(40)


print("PWM bzuziak")
print("Zadaj frekvenciu v Hz (napr. 800), alebo 'melody', alebo 'exit'.")

while True:
    cmd = input("> ").strip().lower()

    if cmd == "exit":
        buzzer.duty(0)
        break

    if cmd == "melody":
        play_melody()
        continue

    try:
        freq = int(cmd)
    except ValueError:
        print("Zadaj cislo, 'melody' alebo 'exit'.")
        continue

    beep(freq)
