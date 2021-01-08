install:
	pip install -r requirements.txt

test:
	python -m pytest tests

lint:
	black .
	flake8
	isort .
