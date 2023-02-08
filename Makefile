test: lint
	ansible-mock --vm

lint:
	flake8 hwz.py
