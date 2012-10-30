init:
	pip install -r requirements.txt --use-mirrors

test:
	nosetests tests

dist:
	python setup.py bdist upload