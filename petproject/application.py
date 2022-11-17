import os
from flask import Flask, render_template
from petproject import dijkstra, astar, general


def create_app(test_config=None):
    app = Flask(__name__, )
    app.config['SECRET_KEY'] = '12345'

    # if test_config is None:
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     app.config.from_pyfile(test_config)
    #
    # # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    app.register_blueprint(general.application)
    app.register_blueprint(dijkstra.application)
    app.register_blueprint(astar.application)

    return app


create_app().run()
