init:
	#pip install -r requirements.txt
	pipenv install

test:
	py.test tests

.PHONY: init test
