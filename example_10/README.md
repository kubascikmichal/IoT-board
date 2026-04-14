# Example 10 - Wi-Fi a posielanie dát na ThingSpeak

Cieľ: pripojiť dosku na Wi-Fi a pravidelne odosielať merania (DHT) na ThingSpeak.

## 1. Registrácia na ThingSpeak

1. Otvor stránku https://thingspeak.mathworks.com.
2. Klikni na Sign Up a vytvor si účet.
3. Potvrď registráciu cez e-mail.
4. Prihlás sa do ThingSpeak.

## 2. Vytvorenie kanála

1. V menu klikni na Channels -> My Channels.
2. Klikni na New Channel.
3. Nastav názov kanála, napr. `IoT Stich board`.
4. Zaškrtni `Field 1` (napr. Temperature) a `Field 2` (napr. Humidity).
5. Klikni na Save Channel.

## 3. API kľúč

1. Otvor svoj kanál.
2. Prejdi na záložku API Keys.
3. Skopíruj `Write API Key`.
4. V súbore `main.py` vlož hodnotu do `THINGSPEAK_API_KEY`.

## 4. Nastavenie Wi-Fi

V `main.py` nastav:

- `WIFI_SSID`
- `WIFI_PASSWORD`

## 5. Spustenie

1. Nahraj `main.py` do dosky.
2. Spusti program.
3. V konzole uvidíš, či sa podarilo poslať dáta.
4. Grafy nájdeš v záložke Private View alebo Public View.

## Poznámky

- ThingSpeak má limit rýchlosti odosielania. Bezpečný interval je aspoň 15 sekúnd.
- V príklade sa odosiela každých 20 sekúnd.
