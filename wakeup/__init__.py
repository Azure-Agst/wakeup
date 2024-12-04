from .config import config
from flask import Flask, g

def create_app():
    app = Flask(__name__)

    from . import home
    app.register_blueprint(home.bp)

    return app