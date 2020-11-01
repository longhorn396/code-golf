.DEFAULT_GOAL := all

all: lint coverage clean

clean:
	@rm -f  .coverage
	@rm -rf __pycache__
	@rm -rf tests/__pycache__

lint:
	-pylint pycg/*.py
	-pylint tests/*.py

coverage:
	coverage run -a -m unittest discover tests
	coverage report

test:
	python3 -m unittest discover tests

image:
	docker build -t pycg .

docker:
	docker run --rm -it -v "$(shell pwd)":/data -w /data pycg
