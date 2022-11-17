from flask import Flask
import main
import dijkstra
import astar


application = Flask(__name__)
application.config['SECRET_KEY'] = '12345'

application.register_blueprint(main.application)
application.register_blueprint(dijkstra.application)
application.register_blueprint(astar.application)

if __name__ == "__main__":
    application.run()
