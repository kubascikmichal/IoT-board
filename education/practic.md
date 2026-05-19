Návrh praktického vyučovania (30 hodín)

Ciele:
- Získať praktické zručnosti v práci s IoT hardvérom a softvérom.
- Navrhnúť, zostaviť a otestovať jednoduché IoT zariadenie.
- Naučiť sa základné meracie postupy, ladenie a dokumentáciu projektu.

Predpoklady:
- Základné znalosti práce s počítačom a programovaním (Python alebo C/C++).
- Základy elektrotechniky (proud, napätie, základné obvody).

Organizácia: 15x2h (30 hodín)

Sessiony (súhrn):
1.  Úvod a bezpečnosť pri práci (2h)
   - Obsah: predstavenie cieľov, bezpečnostné pravidlá pri práci s napätím a nástrojmi, zoznámenie s vybavením (senzory, mikrokontrolér, napájanie).
   - Výstup: študenti vedia bezpečne pracovať so súčiastkami.

2.  Hardvér: prehľad platforiem (2h)
   - Obsah: porovnanie ESP32/Arduino/Raspberry Pi Pico, napájanie, rozhrania (GPIO, I2C, SPI, UART).
   - Výstup: vybranie platformy pre projekt.

3.  Základné zapojenia a merania (2h)
   - Obsah: meranie napätia/prúdu, používanie multimetra, jednoduché obvody s LED a odporom.
   - Výstup: krátky praktický test zapojenia.

4.  Programovanie a nahrávanie firmvéru (2h)
   - Obsah: nastavenie prostredia, jednoduchý "blink" a čítanie digitálneho vstupu.
   - Výstup: bežiaci príklad na každom zariadení.

5.  Analógové vstupy a senzory (2h)
   - Obsah: pripojenie teplotného senzora/čidla svetla, čítanie a kalibrácia.
   - Výstup: zaznamenané merania, graf hodnot.

6.  Komunikačné rozhrania (I2C/SPI/UART) (2h)
   - Obsah: pripojenie senzora cez I2C/SPI, jednoduchá komunikácia cez UART.
   - Výstup: úspešná komunikácia so senzorom.

7.  Bezdrôtová konektivita (Wi‑Fi/BLE) (2h)
   - Obsah: pripojenie k Wi‑Fi, odosielanie jednoduchých HTTP požiadaviek, základy BLE.
   - Výstup: zariadenie odosiela údaje na lokálny server alebo mobil.

8.  Zber dát a lokálne ukladanie (2h)
   - Obsah: ukladať namerané hodnoty do lokálneho súboru alebo jednoduchého DB (napr. SQLite, SPIFFS).
   - Výstup: lokálny záznam meraní.

9.  Základy backendu: jednoduché REST API (2h)
   - Obsah: ukážka jednoduchého servera (Flask / Node.js) prijímajúceho údaje.
   - Výstup: POST endpoint prijíma údaje zo zariadenia.

10. Integrácia senzora do projektu (2h)
    - Obsah: študenti vyberú senzor, implementujú čítanie a základné spracovanie dát.
    - Výstup: funkčný modul senzora.

11. Edge processing a filtrácia dát (2h)
    - Obsah: základné filtre, priemerovanie, debouncing, thresholding.
    - Výstup: spracované a stabilné hodnoty.

12. Napájanie a energetická efektívnosť (2h)
    - Obsah: režimy spánku, meranie odberu, návrh batériového napájania.
    - Výstup: odhad výdrže pri rôznych režimoch.

13. Bezpečnosť a autentifikácia (2h)
    - Obsah: základy šifrovania, bezpečné odosielanie údajov, jednoduchá autentifikácia.
    - Výstup: implementované základné bezpečnostné opatrenia.

14. Testovanie a ladenie projektu (2h)
    - Obsah: diagnostika problémov, logovanie, používanie serial monitoru a oscilloskopu (ak dostupný).
    - Výstup: zoznam odhalených chýb a nápravných krokov.

15. Záverečný projekt a prezentácia (2h)
    - Obsah: dokončenie projektu, príprava krátkej prezentácie a dokumentácie (technická správa, schémy).
    - Výstup: prezentácia výsledkov a demo funkčného zariadenia.

Hodnotenie:
- Priebežné malé úlohy po každej lekcii (praktické overenia).
- Záverečný projekt (funkčné demo + dokumentácia) 60%.
- Aktivita a dodržanie bezpečnostných postupov 10%.
- Krátke písomné/ústne zhrnutie po ostatných témach 30%.

Materiály a pomôcky:
- Zostava mikrokontroléra (ESP32 alebo Arduino), senzory (teplota, vlhkosť, svetlo), napájanie, vodiče, breadboard.
- Počítač s nainštalovaným vývojovým prostredím, multimetr, prípadne malý oscilloskop.

Poznámka: obsah možno upraviť podľa vybavenia a predchádzajúcich skúseností študentov.