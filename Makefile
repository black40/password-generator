APP = main.py

# path to virtualenv bin directory
VENV_BIN := .venv/bin
# prefer ruff from the virtualenv when available, otherwise use ruff from PATH
RUFF := $(if $(wildcard $(VENV_BIN)/ruff),$(VENV_BIN)/ruff,ruff)

run:
	uv run $(APP)


check:
	$(RUFF) check .


fix:
	$(RUFF) check . --fix


format:
	$(RUFF) format .

install:
	uv pip install -r requirements.txt || uv pip install .

PYTHON := $(if $(wildcard .venv/bin/python),.venv/bin/python,python3)

test:
	$(PYTHON) -m unittest discover -s tests

clean:
	rm -rf __pycache__ app/__pycache__ .ruff_cache .pytest_cache build dist