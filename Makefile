init:
	#pip install -r requirements.txt
	pipenv install

test:
	py.test tests
	mypy tcg

.PHONY: init test
