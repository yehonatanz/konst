all: format test

format:
	isort --recursive -y . 
	black .

test-format:
	isort -c -rc .
	black --check .

clean:
	find -name *.py[co] -delete
	find -name __pycache__ -delete

test: clean	
	py.test tests --cov=konst --cov=tests

watch: clean
	ptw

install:
	pip install .

dev:
	pip install -e .[dev]

pre-commit: test-format test
