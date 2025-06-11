.PHONY: indent

luatex:
	latexmk -f -synctex=1 -interaction=nonstopmode \
                 -file-line-error \
                 -lualatex \
                 -outdir=build \
                 main.tex \
 
# sa fie toate in mod normal igig sa le formateze
FILES = chapters/*.tex

# daca dai target oricare fisier in specific sa-l proceseze pe el numa direct ($@ e fix fisieru pe care e tagetu, numele lui)
%.tex:
	latexindent --silent --overwrite -c=build $@

# ok kinda stupid ca gen nu-i de parca am schimbat FILES-u ala
indent:
	latexindent --silent --overwrite -c=build $(FILES)


#curata alea logurile si backuprile de la latexindent, daca tot din cauza lui a trbuit sa fac makefilu asta, macar sa fie si un target de cleanup la el
clean_indent:
	rm build/*.bak*
	rm build/indent.log
	rm -rf build/chapters


