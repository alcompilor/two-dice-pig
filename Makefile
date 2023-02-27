# Running make without specifying options will result in running init #
.DEFAULT_GOAL := init

# Init project by installing all required dependencies #
init: requirements.txt
	pip install -r requirements.txt

# Run flake8 on a specified directory #
flake8:
	@printf "\n\e[\033[0;45m\e[1m LINTING: \e[0m\n"
	@printf "\n\e[\033[0;44m\e[1m FLAKE8 REPORT: \e[0m\n"
	-flake8 $(dir)/*.py
	@printf "\n"

# Run pylint on a specified directory #
pylint:
	@printf "\n\e[\033[0;44m\e[1m PYLINT REPORT: \e[0m\n"
	-pylint $(dir)/*.py
	@printf "\n"

# Run pylint and flake8 together #
lint: flake8 pylint

# Generate uml for the project #
uml:
	-pyreverse -o png ./src

# Run coverage and unittest on a specified directory #
coverage:
	@printf "\n\e[\033[0;45m\e[1m UNIT TESTING: \e[0m\n"
	@printf "\n\e[\033[0;42m\e[1m COVERAGE DONE: \e[0m\n"
	-coverage run --omit=$(dir)/test_*.py -m unittest discover -s $(dir) -p "test_*.py"
	@printf "\n"
	@printf "\n\e[\033[0;42m\e[1m COVERAGE EXPORTED: \e[0m\n"
	-coverage html -d $(dir)/htmlcov
	@printf "\n"
	@printf "\n\e[\033[0;44m\e[1m COVERAGE REPORT: \e[0m\n"
	-coverage report -m
	@printf "\n"

# Run lint and coverage on a specified directory #
test: lint coverage

# Run doc on a specified module #
doc:
	python -m pydoc $(module)