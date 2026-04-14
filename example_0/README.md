# Example 0 - Test dosky

Toto je uvodny servisny test pred dalsimi cviceniami.
Ciel je overit, ze vsetky periferie na DPS funguju a ze sa neprejavuju studene spoje.

## Co test kontroluje

- OLED displej (I2C)
- RGB LED (3 samostatne kanaly)
- Seriove RGB LED (WS2812)
- Bzuziak (PWM)
- Tlacidla USR1 az USR4
- Fotorezistor (ADC)
- DHT senzor (teplota a vlhkost)

## Spustenie

1. Nahraj `main.py` do dosky.
2. Spusti program.
3. Sleduj pokyny v konzole.
4. Na konci skontroluj sumar PASS/FAIL.

## Kontrola studenych spojov

Pocas testu jemne poklep na DPS alebo velmi jemne pohni doskou.
Ak sa pri tom testovana periferia nahodne odpaja, blika nestabilne, alebo hodnoty skacu bez dovodu,
je to podozrenie na studeny spoj a treba skontrolovat spajkovanie.
