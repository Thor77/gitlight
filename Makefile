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

# Run tests
#   -r requirements/tests.txt
test:
	pytest

# Build code coverage map
#   -r requirements/tests.txt
coverage:
	mkdir -p _build
	coverage run --rcfile=tests/.coveragerc -m pytest
	coverage html --rcfile=tests/.coveragerc
	coverage xml --rcfile=tests/.coveragerc

# Print coverage to console
cov-text: coverage
	coverage report --rcfile=tests/.coveragerc

# Open coverage in browser
cov-html: coverage
	sensible-browser _build/htmlcov/index.html

# Upload code coverage map to codacy
# NOTE: Used by build system only
#   -r requirements/tests.txt
upload-coverage: coverage
	ifneq ($(CODACYCOV),no)
		export CODACY_PROJECT_TOKEN=$(CODACYCOV)
		python-codacy-coverage -r _build/coverage.xml
	endif

.PHONY: clean run docs test coverage cov-text cov-html upload-coverage
