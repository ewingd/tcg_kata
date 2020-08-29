init:
	#pip install -r requirements.txt
	pipenv install

test:
	py.test tests
	mypy tcg

lint:
	black tcg/
	black tests/

.PHONY: init test lint
