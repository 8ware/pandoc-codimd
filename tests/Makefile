# Borrowed from https://github.com/jgm/pandocfilters

ALLSAMPLES = $(basename $(wildcard *-sample.md))
ALLPDF = $(addsuffix .pdf,$(ALLSAMPLES))


all: ${ALLPDF}

%.pdf: %.md
	../scripts/preprocess.sh $< \
		| pandoc -F ../codimd/$(subst -sample.md,.py,$<) -o $@

clean:
	$(RM) ${ALLPDF} *.pyc

