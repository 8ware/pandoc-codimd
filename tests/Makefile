# Borrowed from https://github.com/jgm/pandocfilters

ALLSAMPLES = $(basename $(wildcard *-sample.md))
ALLPDF = $(addsuffix .pdf,$(ALLSAMPLES))


all: ${ALLPDF}

%.pdf: %.md
	pandoc --filter ../codimd/$(subst -sample.md,.py,$<) $< -o $@

clean:
	$(RM) ${ALLPDF} *.pyc

