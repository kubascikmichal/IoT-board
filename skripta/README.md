Skriptá k predmetu IoT a vstavané systémy

Obsah:
- `main.tex` – hlavný LaTeX dokument.
- `sections/` – jednotlivé kapitoly: embedded systems, ESP32, MicroPython, príklady.
- `references.bib` – bibliografia.
- `Makefile` – návod na kompiláciu (`make` alebo `latexmk -pdf main.tex`).

Poznámky:
- Kódy sú vkladané pomocou `\lstinputlisting` z priečinkov `example_*` v koreňovom adresári projektu.
- Pri kompilácii sa uistite, že majú LaTeX balíky `listings`, `biblatex` a `latexmk` sú nainštalované.

Príklad kompilácie:

```sh
cd skripta
make
```
