import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev', 
        DATABASE=os.path.join(app.instance_path, 'database.sqlite'),
        )

    if test_config is None:
        # if not testing, load instance config
        app.config.from_pyfile('config.py', silent=True)
    else:
        # if test config is passed in, load it
        app.config.from_mapping(test_config)
    
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # temporary page for testing
    @app.route('/hello')
    def hello():
        return 'Hello, %username%!'

    # :D
    from . import helpers
    helpers.init_app(app)

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app