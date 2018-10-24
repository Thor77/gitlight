'''
GitLight Bootstrap
'''
import flask
import os


def create_app(test_config=None):
    '''Create and configure an instance of the GitLight application.'''
    app = flask.Flask(__name__, instance_relative_config=True)

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

    # register the database commands
    #from gitlight import db
    #db.init_app(app)

    # apply the blueprints to the app
    from .gitlight import gitlight as gl_blueprint
    app.register_blueprint(gl_blueprint)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule('/', endpoint='index')

    return app

#config_name = os.environ.get('FLASK_CONFIG', 'development')
#app.config.from_object('conf/' + config_name)
