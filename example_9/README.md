# Example 9 - Wi-Fi AP a webová stránka

Cieľ: doska vytvorí vlastnú Wi-Fi sieť (AP) a spustí webovú stránku.
Na stránke uvidíš dáta z DHT a tlačidlá na ovládanie:

- sériových RGB LED (WS2812),
- RGB LED (R/G/B),
- bzučiaka,
- OLED displeja.

## Zapojenie (podľa schémy)

- DHT: IO18 (`DHT_DATA`)
- WS2812: IO4 (`LED_PIN`)
- RGB LED: IO7 (`R`), IO5 (`G`), IO3 (`B`)
- Bzučiak: IO11 (`BUZZER_PIN`)
- OLED I2C: SDA IO1, SCL IO2

## Spustenie

1. Nahraj `main.py` do dosky.
2. Doska vytvorí AP sieť `IoTStich-AP` (heslo v kóde).
3. Pripoj sa mobilom alebo notebookom na túto sieť.
4. Otvor IP adresu `192.168.4.1` v prehliadači.
5. Ovládaj periférie cez webové tlačidlá.

## Poznámka

Ak OLED alebo WS2812 knižnica nie je dostupná, príslušná časť sa preskočí,
ale webserver a ostatné periférie budú fungovať ďalej.
