from flask import Flask

from src.views.index_view import bp as bp_index


def create_app():
    app = Flask(__name__)

    app.register_blueprint(bp_index)

    return app
