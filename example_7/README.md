# Example 7 - Citanie a aproximacia fotorezistora (min-max)

Ciel: nacitat analogovu hodnotu z fotorezistora a prepocitat ju na percenta.

## Zapojenie (podla schemy)

- Fotorezistor vstup: IO16 (`PHOTO`)

## Ako funguje aproximacia

1. Program nazbiera viac merani.
2. Najde minimalnu a maximalnu hodnotu.
3. Aktualnu hodnotu prepocita na 0-100 percent.

## Spustenie

1. Nahraj subor `main.py` do dosky.
2. Sleduj vypis v konzole.
3. Men svetlo nad fotorezistorom a pozoruj percenta.
