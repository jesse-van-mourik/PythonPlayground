from flask import Flask
import main
import dijkstra
import astar


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '12345'

    app.register_blueprint(main.application)
    app.register_blueprint(dijkstra.application)
    app.register_blueprint(astar.application)

    return app


if __name__ == "__main__":
    create_app().run()
