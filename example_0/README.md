# Example 0 - Test dosky

Toto je úvodný servisný test pred ďalšími cvičeniami.
Cieľ je overiť, že všetky periférie na DPS fungujú a že sa neprejavujú studené spoje.

## Čo test kontroluje

- OLED displej (I2C)
- RGB LED (3 samostatné kanály)
- Sériové RGB LED (WS2812)
- Bzučiak (PWM)
- Tlačidlá USR1 až USR4
- Fotorezistor (ADC)
- DHT senzor (teplota a vlhkosť)

## Spustenie

1. Nahraj `main.py` do dosky.
2. Spusti program.
3. Sleduj pokyny v konzole.
4. Na konci skontroluj sumár PASS/FAIL.

## Kontrola studených spojov

Počas testu jemne poklep na DPS alebo veľmi jemne pohni doskou.
Ak sa pri tom testovaná periféria náhodne odpája, bliká nestabilne, alebo hodnoty skáču bez dôvodu,
je to podozrenie na studený spoj a treba skontrolovať spájkovanie.
