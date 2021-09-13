LATEXMK ?= latexmk

.PHONY: all clean

all: a1.zip

# remember to add other assignments...
# there's some makefile magic

a1/a1.pdf: a1/a1.tex $(shell find a1/figs)
	${LATEXMK} -silent -cd -pdf $<
	${LATEXMK} -silent -cd -c $<

a1.zip: a1/a1.pdf $(shell find a1)
	rm -f $@
	zip -rX $@ $^
