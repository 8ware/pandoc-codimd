# Borrowed from https://github.com/jgm/pandocfilters

ALLSAMPLES = $(basename $(wildcard *-sample.md))
ALLPDF = $(addsuffix .pdf,$(ALLSAMPLES))


all: ${ALLPDF}

%.pdf: %.md
	../scripts/preprocess.sh $< \
		| pandoc -F ../codimd/$(subst -sample.md,.py,$<) -o $@

%.tex: %.md
	../scripts/preprocess.sh $< \
		| pandoc -F ../codimd/$(subst -sample.md,.py,$<) -o $@

codimd-features.md:
	wget -O codimd-features.md https://demo.codimd.org/features/download

%-features.pdf: %-features.md
	(cat unicode.yaml; ../scripts/preprocess.sh $<) \
		| pandoc -F ../codimd.py -o $@

clean:
	$(RM) ${ALLPDF} *.pyc *.tex *-features.pdf *-features.md

