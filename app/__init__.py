'''
GitLight Bootstrap
'''
import os
from flask import Flask


def create_app():
    config_name = os.environ.get('FLASK_CONFIG', 'development')

    app = Flask(__name__)
    app.config.from_object('conf/' + config_name)

    mongo.init_app(app)

    from .gitlight import gitlight as gl_blueprint
    app.register_blueprint(gl_blueprint)

    return app
