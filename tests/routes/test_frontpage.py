#!/usr/bin/env python3
'''
Test routes for frontpage.
'''
# Python / Flask Ipmorts
import flask

# GitLight Imports
from gitlight.routes import frontpage


def test_blueprint():
    '''
    Test building blueprint.
    '''
    # Get blueprint
    app = flask.Flask(__name__)
    app.register_blueprint(frontpage.bp)


def test_index():
    '''
    Test index route.
    '''
    # Page contains expected text
    assert b'Gitea' in frontpage.index()
