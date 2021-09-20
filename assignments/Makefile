LATEXMK ?= latexmk

.PHONY: all clean

all: a1.zip a1sol.zip

# to add other assignments:
#   - put as a target of all
#   - put the extra dependency rules for the pdf and zip

a1/a1.pdf: $(shell find a1/figs)
%.pdf: %.tex
	${LATEXMK} -silent -cd -pdf -shell-escape $<

a1.zip: a1/a1.pdf $(shell find a1/code a1/data a1/figs)
%.zip: %
	# clean up tex tmp files
	${LATEXMK} -silent -cd -c $</*.tex
	rm -rf $</_minted-*
	# delete existing zip
	rm -f $@
	# make new zip
	zip -rX $@ $< -x '*__pycache__*' -x '*.DS_Store' -x '*.ipynb_checkpoints*'
