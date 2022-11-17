import os
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = '12345'

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_pyfile(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from petproject import application
    app.register_blueprint(application.application)

    # from petproject.Excluded import movement
    # app.register_blueprint(movement.application)

    from petproject import dijkstra
    app.register_blueprint(dijkstra.application)

    from petproject import astar
    app.register_blueprint(astar.application)

    return app


create_app(create_app).run(host='localhost', port=8080)
