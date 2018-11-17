format:
	isort -ot -rc -y .
	black -S --py36 .

clean:
	find -name *.py[co] -delete
	find -name __pycache__ -delete

test: clean
	py.test tests

watch: clean
	ptw

install:
	pip install .

dev:
	pip install -e .[dev]

pre-commit: format test
