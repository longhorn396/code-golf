.DEFAULT_GOAL := all

all: clean lint coverage

clean:
	rm -f  .coverage
	rm -rf __pycache__

lint:
	-pylint *.py

coverage:
	coverage run -a -m unittest discover
	coverage report

tests:
	python -m unittest discover
	