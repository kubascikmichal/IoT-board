from machine import Pin
import time


# Pin mapping podla schemy
BTN_PINS = [39, 37, 35, 33]


def wait_release(button: Pin) -> None:
    while button.value() == 0:
        time.sleep_ms(20)


def generate_target_from_buttons() -> int:
    buttons = [Pin(pin, Pin.IN) for pin in BTN_PINS]
    entropy = 0
    press_count = 8

    print("Generovanie cisla z tlacidiel USR1-USR4")
    print("Stlac %d-krat lubovolne tlacidla..." % press_count)

    while press_count > 0:
        for idx, btn in enumerate(buttons):
            if btn.value() == 0:
                # Tlacidlo + cas stlacenia vytvoria pseudo-nahodny seed.
                entropy = (entropy * 37 + (idx + 1) * 17 + time.ticks_ms()) & 0x7FFFFFFF
                press_count -= 1
                print("Stlacenie %d/%d" % (8 - press_count, 8))
                wait_release(btn)
                time.sleep_ms(30)

    return (entropy % 100) + 1


def main() -> None:
    target = generate_target_from_buttons()
    attempts = 0

    print("Hadaj cislo od 1 do 100")

    while True:
        raw = input("Zadaj tip: ").strip()

        if not raw.isdigit():
            print("Zadaj cele cislo.")
            continue

        guess = int(raw)
        attempts += 1

        if guess < target:
            print("Malo.")
        elif guess > target:
            print("Vela.")
        else:
            print(f"Spravne. Pocet pokusov: {attempts}")
            break


if __name__ == "__main__":
    main()
