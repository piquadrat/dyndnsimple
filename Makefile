init:
	pip install -r requirements.txt --use-mirrors

test:
	nosetests tests

publish:
	python setup.py sdist upload