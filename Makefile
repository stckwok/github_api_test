install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
install_win:
	python.exe -m pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code
	black github_api.py
lint:
	pylint --disable=R,C github_api.py
test:
	python -m pytest -vv --cov=github_api tests/github_api_test.py

all: install format lint test
