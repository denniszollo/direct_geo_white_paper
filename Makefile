all:
	make plot
	make pdf 
plot: generate_plots.py data
	python generate_plots.py

pdf: whitepaper.tex
	pdflatex whitepaper.tex

