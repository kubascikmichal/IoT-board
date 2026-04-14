# IoT-board

Tento repozitar obsahuje ukazkove projekty pre dosku IoT Stich board.
Je pripravena tak, aby sa s nou dalo jednoducho cvicit na hodinach.

## Struktura repozitara

```text
.
|- LICENSE
|- README.md
`- docs/
	`- schematic.pdf
```

Planovana dokumentacia v priecinku `docs/`:

- `schematic.pdf` - elektricka schema dosky
- `board-photo.*` - fotografia dosky (napr. JPG/PNG)

## IoT Stich board - popis

Doska je postavena na module WEMOS S2 MINI (ESP32-S2).
Najdes na nej bezne suciastky, s ktorymi sa pracuje pri IoT projektoch:

- MCU modul: WEMOS S2 MINI (ESP32-S2)
- Displej: OLED na I2C zbernici
- RGB LED: retazce WS2812B (interny segment + externy vystup)
- Tlacidla: 4x uzivatelske tlacidlo (`USR1_BTN` az `USR4_BTN`)
- Senzory a periferie: DHT, fotoodpor (`PHOTO`), bzuziak (`BUZZER`)
- Napajanie: vetvy `+5V`, `3V3`, `GND`

## Ako s tym zacat

1. Otvor si schemu v subore `docs/schematic.pdf`.
2. Spusti `example_0` (Test dosky), aby si overil periferie a spoje.
3. Pozri si tabulku nizsie a najdi, na ktorom pine je dana suciastka.
4. V priklade potom nastav spravny pin podla tejto tabulky.
5. Otestuj zapojenie po castiach (napr. najprv tlacidlo, potom LED).

## Fotka dosky

Po pridani obrazka do `docs/` je mozne pouzit napr. tento odkaz:

![IoT Stich board](docs/board-photo.jpg)

## Mapovanie pinov (podla `docs/schematic.pdf`)

Toto je najdolezitejsia cast pre programovanie.
Ak si nie si isty, vzdy sa vrat na schemu a over signal.

### Priame signaly MCU

| Signal | GPIO (ESP32-S2) | Poznamka |
|---|---:|---|
| I2C_SDA | IO1 | OLED data |
| I2C_SCL | IO2 | OLED clock |
| LED_PIN | IO4 | riadenie LED vetvy |
| USR1_BTN | IO39 | uzivatelske tlacidlo 1 |
| USR2_BTN | IO37 | uzivatelske tlacidlo 2 |
| USR3_BTN | IO35 | uzivatelske tlacidlo 3 |
| USR4_BTN | IO33 | uzivatelske tlacidlo 4 |
| DHT_DATA | IO18 | data z DHT senzora |
| PHOTO | IO16 | vstup z fotoodporu |

### Farebna RGB vetva a audio

| Signal | GPIO (ESP32-S2) | Poznamka |
|---|---:|---|
| LED_PIN_B | IO3 | modry kanal RGB |
| LED_PIN_G | IO5 | zeleny kanal RGB |
| LED_PIN_R | IO7 | cerveny kanal RGB |
| BUZZER_PIN | IO11 | riadenie bzuziaka |

### LED retazce WS2812B

V scheme su oznacene datove vetvy:

- `LED_DATA_1`
- `LED_DATA_2`
- `LED_DATA_EXT` (vyvedeny externy vystup `LED_OUT1`)

## Poznamky k pouzitiu

- Pred nahratim prikladov si skontrolujte, ktore periferie su na doske osadene.
- Pri aktualizacii hardveru udrziavajte README v sulade s `docs/schematic.pdf`.
- Ked nieco nefunguje, najprv skontroluj pin, napajanie a GND.
