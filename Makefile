clean:
	rm -rf .venv

env:
	python3 -m venv .venv

install:
	python3 -m venv .venv && .venv/bin/pip3 install --upgarde pip && .venv/bin/pip3 install poetry && .venv/bin/poetry install

run:
	.venv/bin/python3 app/main.py