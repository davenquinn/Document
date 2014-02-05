BIBFILE = /Users/Daven/Resources/Papers/bibtex/library.bib
BIBSTYLE = /Users/Daven/Resources/LaTeX/CSL/agu.csl
THEME = components/lib/proposition
.PHONY: phonytarget all clean

BUILD = _build
T = skeleton

all: final

initial: start final

shrink:
	gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=dist/dquinn_NESSF_grant_proposal_small.pdf _dist/dquinn_NESSF_grant_proposal.pdf

word:
	$(THEME)/scripts/figures.py --strip document/text/main.md | \
	pandoc -t docx --bibliography=$(BIBFILE) --csl=$(THEME)/csl/agu.csl -o dist/dquinn_NESSF_grant_proposal.docx

pandoc:
	$(THEME)/scripts/figures.py document/text/main.md | \
	pandoc -t latex --natbib -o .build/main.tex;\

start: pandoc
	xelatex -output-directory .build $(THEME)/latex/skeleton.tex;

final: pandoc
	echo "Updating Bibliograpy"; \
	bibtex8 .build/skeleton.aux; \
	xelatex -output-directory .build $(THEME)/latex/skeleton.tex; \
	mv .build/skeleton.pdf dist/dquinn_NESSF_grant_proposal.pdf;


$(BUILD)/$(T).aux: | phonytarget
	@xelatex -output-directory .build components/skeleton.tex;
	
phonytarget:
	@echo what the hack is wrong with you