LATEX := pdflatex
LATEX_ARGS := -halt-on-error -interaction=nonstopmode -output-directory=build

CONVERT := convert
CONVERT_ARGS := -density 300 -units PixelsPerInch
CONVERT_PNG_ARGS := -quality 90

TEX_FILES := $(wildcard *.tex)
TEX_FILES := $(filter-out main.tex,$(TEX_FILES))
PDF_FILES := $(patsubst %.tex,build/%.pdf,$(TEX_FILES))
PNG_FILES := $(patsubst %.tex,build/%.png,$(TEX_FILES))

.PHONY: all clean post_build

all: build $(PNG_FILES) post_build

build/%.png : build/%.pdf
	$(CONVERT) $(CONVERT_ARGS) $< $(CONVERT_PNG_ARGS) $@

build/%.pdf : %.tex
	$(LATEX) $(LATEX_ARGS) -jobname=$(patsubst %.tex,%,$<) main.tex

build:
	mkdir build

clean:
	rm -r build

post_build:
	rm build/*.aux build/*.log
