from flask import Flask, config, redirect

from flask.json import jsonify
import os
from src.constants.http_status_codes import (
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
from src.accounts.models import db


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("DEVELOPMENT_DATABASE_URL"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
        )
    else:
        app.config.from_mapping(test_config)
    db.app = app
    db.init_app(app)

    @app.route("/")
    def hello():
        return "Hello World!"

    from src.accounts import urls

    bookurl = urls.bookurl
    app.register_blueprint(bookurl)

    @app.errorhandler(HTTP_404_NOT_FOUND)
    def handle_404(e):
        return jsonify({"error": "Not found"}), HTTP_404_NOT_FOUND

    @app.errorhandler(HTTP_500_INTERNAL_SERVER_ERROR)
    def handle_500(e):
        return (
            jsonify({"error": "Something went wrong, we are working on it"}),
            HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return app
