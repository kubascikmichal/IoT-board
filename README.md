# IoT-board

Tento repozitár obsahuje ukážkové projekty pre dosku IoT Stich board.
Je pripravená tak, aby sa s ňou dalo jednoducho cvičiť na hodinách.

## Štruktúra repozitára

```text
.
|- LICENSE
|- README.md
`- docs/
	`- schematic.pdf
```

Plánovaná dokumentácia v priečinku `docs/`:

- `schematic.pdf` - elektrická schéma dosky
- `board-photo.*` - fotografia dosky (napr. JPG/PNG)

## IoT Stich board - popis

Doska je postavená na module WEMOS S2 MINI (ESP32-S2).
Nájdeš na nej bežné súčiastky, s ktorými sa pracuje pri IoT projektoch:

- MCU modul: WEMOS S2 MINI (ESP32-S2)
- Displej: OLED na I2C zbernici
- RGB LED: reťazce WS2812B (interný segment + externý výstup)
- Tlačidlá: 4x používateľské tlačidlo (`USR1_BTN` až `USR4_BTN`)
- Senzory a periférie: DHT, fotoodpor (`PHOTO`), bzučiak (`BUZZER`)
- Napájanie: vetvy `+5V`, `3V3`, `GND`

## Ako s tým začať

1. Otvor si schému v súbore `docs/schematic.pdf`.
2. Spusti `example_0` (Test dosky), aby si overil periférie a spoje.
3. Pozri si tabuľku nižšie a nájdi, na ktorom pine je daná súčiastka.
4. V príklade potom nastav správny pin podľa tejto tabuľky.
5. Otestuj zapojenie po častiach (napr. najprv tlačidlo, potom LED).

## Fotka dosky

Po pridaní obrázka do `docs/` je možné použiť napr. tento odkaz:

![IoT Stich board](docs/board-photo.jpg)

## Mapovanie pinov (podľa `docs/schematic.pdf`)

Toto je najdôležitejšia časť pre programovanie.
Ak si nie si istý, vždy sa vráť na schému a over signál.

### Priame signály MCU

| Signál | GPIO (ESP32-S2) | Poznámka |
|---|---:|---|
| I2C_SDA | IO1 | OLED dáta |
| I2C_SCL | IO2 | OLED clock |
| LED_PIN | IO4 | riadenie LED vetvy |
| USR1_BTN | IO39 | používateľské tlačidlo 1 |
| USR2_BTN | IO37 | používateľské tlačidlo 2 |
| USR3_BTN | IO35 | používateľské tlačidlo 3 |
| USR4_BTN | IO33 | používateľské tlačidlo 4 |
| DHT_DATA | IO18 | dáta z DHT senzora |
| PHOTO | IO16 | vstup z fotoodporu |

### Farebná RGB vetva a audio

| Signál | GPIO (ESP32-S2) | Poznámka |
|---|---:|---|
| LED_PIN_B | IO3 | modrý kanál RGB |
| LED_PIN_G | IO5 | zelený kanál RGB |
| LED_PIN_R | IO7 | červený kanál RGB |
| BUZZER_PIN | IO11 | riadenie bzučiaka |

### LED reťazce WS2812B

V schéme sú označené dátové vetvy:

- `LED_DATA_1`
- `LED_DATA_2`
- `LED_DATA_EXT` (vyvedený externý výstup `LED_OUT1`)

## Poznámky k použitiu

- Pred nahratím príkladov si skontrolujte, ktoré periférie sú na doske osadené.
- Pri aktualizácii hardvéru udržiavajte README v súlade s `docs/schematic.pdf`.
- Keď niečo nefunguje, najprv skontroluj pin, napájanie a GND.
