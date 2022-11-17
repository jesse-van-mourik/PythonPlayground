import os
from flask import Flask, render_template
from petproject import dijkstra, astar, general


def create_app(test_config=None):
    application = Flask(__name__, )
    application.config['SECRET_KEY'] = '12345'

    # if test_config is None:
    #     application.config.from_pyfile('config.py', silent=True)
    # else:
    #     application.config.from_pyfile(test_config)
    #
    # # ensure the instance folder exists
    # try:
    #     os.makedirs(application.instance_path)
    # except OSError:
    #     pass

    application.register_blueprint(general.application)
    application.register_blueprint(dijkstra.application)
    application.register_blueprint(astar.application)

    return application


if __name__ == "__main__":
    create_app().run(host='localhost', port=8080)
