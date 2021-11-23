LATEXMK ?= latexmk

.PHONY: all clean

all: a1.zip a2.zip a3.zip a4.zip a5.zip a6.zip

# to add other assignments:
#   - put as a target of all
#   - put the extra dependency rules for the pdf and zip

a1/a1.pdf: $(shell find a1/figs)
a2/a2.pdf: $(shell find a2/figs)
a3/a3.pdf: $(shell find a3/figs)
a4/a4.pdf: $(shell find a4/figs)
a5/a5.pdf: $(shell find a5/figs)
a6/a6.pdf: $(shell find a5/figs)
%.pdf: %.tex
	${LATEXMK} -silent -cd -pdf -shell-escape $<

a1.zip: a1/a1.pdf $(shell find a1/code a1/data a1/figs)
a2.zip: a2/a2.pdf $(shell find a2/code a2/data a2/figs)
a3.zip: a3/a3.pdf $(shell find a3/code a3/data a3/figs)
a4.zip: a4/a4.pdf $(shell find a4/code a4/data a4/figs)
a5.zip: a5/a5.pdf $(shell find a5/code a5/data a5/figs)
a6.zip: a6/a6.pdf $(shell find a6/code a6/data a6/figs)
%.zip: %
	# clean up tex tmp files
	${LATEXMK} -silent -cd -c $</*.tex
	rm -rf $</_minted-*
	# delete existing zip
	rm -f $@
	# make new zip
	zip -rX $@ $< -x '*__pycache__*' -x '*.DS_Store' -x '*.ipynb_checkpoints*'
