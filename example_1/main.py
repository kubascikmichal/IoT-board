import random


def main() -> None:
    target = random.randint(1, 100)
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
