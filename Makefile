.PHONY: indent

# Default value for FILES if none is provided on the command line
# You can set this to process all .tex files in the current directory by default,
# or leave it empty requiring files to be specified.
FILES = chapters/*.tex

indent:
	# Use the FILES variable in the command
	latexindent --silent --overwrite $(FILES)
