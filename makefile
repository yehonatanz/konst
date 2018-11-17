all: format test

format:
	isort --recursive -y . 
	black .

test-format:
	isort -c -rc .
	black --check .

clean:
	# This resloves to find on both unix and windows git bash environments
	`which -a find | grep usr | head -n1` -name *.py[co] -delete
	`which -a find | grep usr | head -n1` -name __pycache__ -delete

test: clean
	py.test tests --cov=konst --cov=tests

watch: clean
	ptw

install:
	pip install .

dev:
	pip install -e .[dev]

clean-dist:
	rm -rf dist/ build/

dist: format test clean-dist
	python setup.py sdist bdist_wheel

publish: dist
	twine upload dist/*

pre-commit: test-format test
