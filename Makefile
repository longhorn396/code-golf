.DEFAULT_GOAL := all

all: lint coverage clean

clean:
	@rm -f  .coverage
	@rm -rf __pycache__
	@rm -rf tests/__pycache__

lint:
	-pylint *.py
	-pylint tests/*.py

coverage:
	coverage run -a -m unittest discover tests
	coverage report

test:
	python3 -m unittest discover tests
	