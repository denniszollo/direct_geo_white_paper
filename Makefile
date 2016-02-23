all:
	make plot
	make pdf 
plot:
	python generate_plots.py

pdf: whitepaper.tex
	pdflatex whitepaper.tex

