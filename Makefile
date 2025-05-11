.PHONY: indent

# Default value for FILES if none is provided on the command line
# You can set this to process all .tex files in the current directory by default,
# or leave it empty requiring files to be specified.
FILES = chapters/*.tex

# Pattern rule to process any .tex file when it's given as a target
%.tex:
	latexindent --silent --overwrite -c=build $@

indent:
	# Use the FILES variable in the command
	latexindent --silent --overwrite -c=build $(FILES)


#curata alea logurile si backuprile de la latexindent, daca tot din cauza lui a trbuit sa fac makefilu asta, macar sa fie si un target de cleanup la el
clean_indent:
	rm build/*.bak*
	rm build/indent.log
	rm -rf build/chapters


