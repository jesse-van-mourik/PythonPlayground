import os
from flask import Flask, render_template
import dijkstra
import astar
import general


def create_app(test_config=None):

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

    return application


application = Flask(__name__)
application.register_blueprint(general.application)
application.register_blueprint(dijkstra.application)
application.register_blueprint(astar.application)


if __name__ == "__main__":
    application.run()
