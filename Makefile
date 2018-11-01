FLASK_APP ?= gitlight
FLASK_ENV ?= testing
CODACYCOV += no
export FLASK_APP FLASK_ENV CODACYCOV

# Clean up build/cache data
clean:
	@find . -name '*.pyc' \
		-o -name '__pycache__' \
		-o -name '.pytest_cache' \
		-o -name '*,cover' \
		-exec rm -rf {} +;
	@rm -rf _build

# Run a development web server
#   -r requirements/base.txt
run:
	export FLASK_ENV=development
	flask run

# Build local copy of documentation
#   -r requirements/docs.txt
docs:
	mkdir -p _build
	sphinx-build docs/ _build/docs/

# Run all tests
#   -r requirements/tests.txt
test: unit integration

# Run unit tests
#   -r requirements/tests.txt
unit:
	pytest

# Run unit integration
#   -r requirements/tests.txt
integration:
	#TODO

# Build code coverage map
#   -r requirements/tests.txt
coverage:
	mkdir -p _build
	coverage run --rcfile=tests/.coveragerc -m pytest
	# `make coverage-text` to view in console
	# `make coverage-view` to view in web browser

# Print coverage to console
coverage-text: coverage
	coverage report --rcfile=tests/.coveragerc

# Open coverage in browser
coverage-html: coverage
	coverage html --rcfile=tests/.coveragerc
	sensible-browser _build/htmlcov/index.html

# Upload code coverage map to codacy
# NOTE: Used by build system only
#   -r requirements/tests.txt
upload-coverage: coverage
	ifneq ($(CODACYCOV),no)
		#TODO
	endif

.PHONY: clean run docs test unit integration coverage coverage-text coverage-html
