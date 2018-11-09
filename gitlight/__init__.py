#!/usr/bin/env python3
'''
GitLight Bootstrap
'''
# Python / Flask Imports
import os
import flask

# GitLight Imports
#from gitlight.lib import db
from gitlight.routes import frontpage

def create_app(test_config=None):
    '''
    Create and configure an instance of the GitLight application.
    '''
    app = flask.Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register database commands
    #db.init_app(app)

    # apply blueprints to the app
    app.register_blueprint(frontpage.bp)

    # make url_for('index') == url_for('frontpage.index')
    app.add_url_rule('/', endpoint='index')

    return app
