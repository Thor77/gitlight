#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
GitLight/Flask things for pytest
'''
import pytest
from gitlight import create_app


@pytest.fixture
def app():
    '''Create and configure a new app instance for each test'''
    # create a temporary file to isolate the database for each test
    #db_fd, db_path = tempfile.mkstemp()
    # create the app with common test config
    app = create_app({
        'TESTING': True,
        #'DATABASE': db_path,
    })

    # create the database and load test data
    #with app.app_context():
    #    init_db()
    #    get_db().executescript(_data_sql)

    yield app

    # close and remove the temporary database
    #os.close(db_fd)
    #os.unlink(db_path)


@pytest.fixture
def client(app):
    '''A test client for the app'''
    return app.test_client()


@pytest.fixture
def runner(app):
    '''A test runner for background tasks'''
    return app.test_cli_runner()
