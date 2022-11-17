from flask import Flask
import main
import dijkstra
import astar


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = '12345'

    app.register_blueprint(main.application)
    app.register_blueprint(dijkstra.application)
    app.register_blueprint(astar.application)

    return app


create_app(create_app).run()
