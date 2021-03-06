
from flask import Flask, render_template
import requests
import os
from app.database import db
from app.jwt import jwt

from app.users.routes import users_blueprint
from app.links.routes import links_blueprint
from app.static.routes import static_blueprint
from . import config
from flask_cors import CORS


def create_app(config=config.DevConfig):
    app = Flask(__name__)

    app.config.from_object(config)
    app.url_map.strict_slashes = False
    CORS(app, supports_credentials=True)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)

    return app


def register_extensions(app):
    db.init_app(app)
    jwt.init_app(app)


def register_blueprints(app):
    if os.getenv("SERVE_STATIC") == "1":
        app.register_blueprint(
            static_blueprint)
    app.register_blueprint(
        links_blueprint)
    app.register_blueprint(
        users_blueprint, url_prefix='/users/')


def register_errorhandlers(app):

    def render_error(e): return render_template(
        'errors/%s.jinja' % e.code), e.code

    codes = [
        requests.codes.INTERNAL_SERVER_ERROR,
        requests.codes.NOT_FOUND,
        requests.codes.UNAUTHORIZED,
    ]

    for e in codes:
        app.errorhandler(e)(render_error)
