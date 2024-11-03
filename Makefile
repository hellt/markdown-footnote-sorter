VENV ?= .venv/bin/activate

all: init ruff mdlint yamllint test
.PHONY: all

.PHONY: clean
clean:
	@rm -rf .venv node_modules .ruff_cache __pycache__ tests/__pycache__

# set up the testing environment
.PHONY: init
.ONESHELL:
init:
	@uv venv
	@source .venv/bin/activate
	@uv pip install ruff yamllint
	@deactivate
	@npm install markdownlint-cli2 --save-dev

# run all the linting operations
.PHONY: lint
lint: ruff mdlint yamllint

# markdown linting
.PHONY: mdlint
mdlint:
	@./node_modules/.bin/markdownlint-cli2 *.md tests/*/*.md

# Python linting and formatting
.PHONY: ruff
ruff:
	@source $(VENV)
	@uv run ruff check
	@uv run ruff format --check --diff
	@deactivate

.PHONY: test
test:
	@python -m unittest discover -s tests -v

# yaml linting
.PHONY: yamllint
yamllint:
	@source $(VENV)
	@uv run yamllint .
	@deactivate
