install:
	pip install -r requirements.txt

test:
	pytest

lint:
	black .
	flake8