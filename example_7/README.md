# Example 7 - Čítanie a aproximácia fotorezistora (min-max)

Cieľ: načítať analógovú hodnotu z fotorezistora a prepočítať ju na percentá.

## Zapojenie (podľa schémy)

- Fotorezistor vstup: IO16 (`PHOTO`)

## Ako funguje aproximácia

1. Program nazbiera viac meraní.
2. Nájde minimálnu a maximálnu hodnotu.
3. Aktuálnu hodnotu prepočíta na 0-100 percent.

## Spustenie

1. Nahraj súbor `main.py` do dosky.
2. Sleduj výpis v konzole.
3. Meň svetlo nad fotorezistorom a pozoruj percentá.
