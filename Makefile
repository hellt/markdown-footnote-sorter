.RECIPEPREFIX = >
VENV ?= .venv/bin/activate

RUFF_IMG := ghcr.io/astral-sh/ruff
RUFF_VER := 0.7.2
MDLINT_IMG := davidanson/markdownlint-cli2
MDLINT_VER := v0.14.0
YAMLLINT_IMG := cytopia/yamllint
YAMLLINT_VER := latest

all: lint test
.PHONY: all

.PHONY: clean
clean:
>   @docker rmi ${RUFF_IMG}:${RUFF_VER} \
>    ${MDLINT_IMG}:${MDLINT_VER} \
>    ${YAMLLINT_IMG}:${YAMLLINT_VER}

# run all the linting operations
.PHONY: lint
lint: ruff mdlint yamllint

# markdown linting
# Note: Local security access control (ex: SELinux) will temporarily need to
# 		be disabled for the Docker bind mounts to function.
.PHONY: mdlint
mdlint:
>   @docker run --rm -v ${PWD}:/workdir ${MDLINT_IMG}:${MDLINT_VER}

# Python linting and formatting
.PHONY: ruff
ruff:
>   @docker run --rm -v ${PWD}:/workdir ${RUFF_IMG}:${RUFF_VER} \
>    check /workdir
>   @docker run --rm -v ${PWD}:/workdir ${RUFF_IMG}:${RUFF_VER} \
>    format --check --diff /workdir

# Python unit tests
.PHONY: test
test:
>   @python -m unittest discover -s tests -v

# yaml linting
.PHONY: yamllint
yamllint:
>   @docker run --rm -v ${PWD}:/data ${YAMLLINT_IMG}:${YAMLLINT_VER} .


### LOCAL DEVELOPMENT ###
# (non-containerized)

# clean up caches (ruff, node, py)
.PHONY: localclean
localclean:
>   @rm -rf .venv node_modules .ruff_cache __pycache__ tests/__pycache__

# set up the LOCAL testing environment
.PHONY: localinit
.ONESHELL:
localinit:
>   @uv venv
>   @source .venv/bin/activate
>   @uv pip install ruff yamllint
>   @deactivate
>   @npm install markdownlint-cli2 --save-dev

# remains as an artifact for those who want to use local linting
# LOCAL markdown linting
.PHONY: localmdl
localmdl:
>   @./node_modules/.bin/markdownlint-cli2

# LOCAL Python linting and formatting
.PHONY: localruff
localruff:
>   @source $(VENV)
>   @uv run ruff check
>   @uv run ruff format --check --diff
>   @deactivate

# LOCAL yaml linting
.PHONY: localyaml
localyaml:
>   @source $(VENV)
>   @uv run yamllint .
>   @deactivate
