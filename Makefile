FLASK_APP ?= gitlight
FLASK_ENV ?= testing
CODACYCOV += no
export FLASK_APP FLASK_ENV CODACYCOV

# Clean up build/cache data
clean:
	@find . -name '*.pyc' \
		-o -name '__pycache__' \
		-o -name '.pytest_cache' \
		-exec rm -rf {} \;
	@rm -rf _build

# Create an output directory
_build:
	@mkdir _build

# Run a development web server
#   -r requirements/base.txt
run:
	export FLASK_ENV=development
	flask run

# Build local copy of documentation
#   -r requirements/docs.txt
docs: _build
	sphinx-build docs/ _build/docs/

# Run tests
#   -r requirements/tests.txt
test:
	pytest

# Spell checker (pytest-spellcheck would be better)
#   -r requirements/tests.txt
spell: _build
	find gitlight/ -name '*.py' | misspellings -f - | tee _build/spelling.txt

# Lint checker
#   -r requirements/tests.txt
lint: _build
	pylint --jobs=0 --persistent=n --reports=y gitlight | tee _build/lint.txt

# Build code coverage map
#   -r requirements/tests.txt
coverage: _build
	pytest \
		--cov-config tests/.coveragerc \
		--cov-report=xml \
		--cov-report=html \
		--cov-report=term:skip-covered \
		--cov=gitlight tests/ \
			>_build/coverage.txt

# Print coverage to console
cov-text: coverage
	awk '/- coverage:/{y=1;next}y' _build/coverage.txt

# Open coverage in browser
cov-html: coverage
	sensible-browser _build/htmlcov/index.html

.PHONY: clean run docs test spell lint coverage cov-text cov-html
