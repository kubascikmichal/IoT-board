# Example 4 - SSD displej + prerušenia tlačidiel

Cieľ: použiť 4 tlačidlá v režime prerušenia (IRQ), merať dĺžku stlačenia
a zobrazovať výsledok na OLED displeji aj v konzole.

## Zapojenie (podľa schémy)

- SDA: IO1
- SCL: IO2
- Napájanie: 3V3 a GND
- USR1: IO39
- USR2: IO37
- USR3: IO35
- USR4: IO33

## Čo robí program

1. Nastaví prerušenia na tlačidlách USR1 až USR4 (stlačenie aj uvoľnenie).
2. Pri stlačení si zapamätá čas začiatku.
3. Pri uvoľnení vypočíta dĺžku stlačenia v ms.
4. Zákmity kontaktov filtruje pomocou debounce delay (`DEBOUNCE_MS`).
5. Výsledok vypíše do konzoly a na OLED.

## Spustenie

1. Nahraj súbor `main.py` do dosky.
2. Spusti program.
3. Stláčaj tlačidlá USR1 až USR4.
4. Sleduj dĺžku stlačenia v konzole a na OLED.
5. Program ukončíš cez `Ctrl+C`.
