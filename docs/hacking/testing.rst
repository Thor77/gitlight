GitLight Testing
================

A variety of tools are used to maintain the quality of our code.

Venv & Reqs
-----------

Activate a virtualenv and install requirements:

    . ~/.venv/bin/activate
    pip3 -r requirements/tests.py

Unit Tests
----------

Unit tests should be succinct little bits of code that test specific responses
from functions. For more complete test logic, check out integration tests.'


Run unit tests:

    make unit

Integration Tests
-----------------

Integration tests are larger tests for testing complex logic.

Run integration tests:

    make integration

Code Coverage
-------------

All modifications are expected to come with a unit test. Coverage maps are an
excellent way to catch problems.

Build coverage map:

    make coverage

TODO
