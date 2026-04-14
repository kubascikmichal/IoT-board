# Example 11 - MQTT publish/subscribe s public brokerom

Cieľ: pripojiť sa na Wi-Fi, prihlásiť sa na public MQTT broker,
a ukázať publish aj subscribe v jednom programe.

## Čo je MQTT

- `publish`: odoslanie správy do topicu,
- `subscribe`: odoberanie správ z topicu.

## Public broker (príklad)

V tomto príklade je použitý broker:

- `broker.hivemq.com`
- port `1883`

Poznámka: public broker je zdieľaný všetkými používateľmi, preto si vyber vlastný unikátny topic.

## Nastavenie

V `main.py` nastav:

- `WIFI_SSID`
- `WIFI_PASSWORD`
- `TOPIC`

## Spustenie

1. Nahraj `main.py` do dosky.
2. Program sa pripojí na broker a začne:
   - odoberať správy z topicu,
   - každých 5 sekúnd publikovať novú správu.
3. Správy uvidíš v konzole.

## Overenie z PC

Môžeš použiť napr. MQTT Explorer alebo online MQTT klient a pripojiť sa na rovnaký broker/topic.
