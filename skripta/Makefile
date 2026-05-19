PDF=main.pdf
TEX=main.tex
OUTPUT=skripta.pdf

all: 
	rm -f $(OUTPUT) main.aux main.bbl main.blg main.out main.toc main.run.xml && pdflatex $(TEX) && bibtex main && pdflatex $(TEX) && pdflatex $(TEX) && mv $(PDF) $(OUTPUT)

time:
	date
