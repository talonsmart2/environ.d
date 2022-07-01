from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from os.path import isfile

db = SQLAlchemy()

def app_factory():
    app = Flask(__name__)
    app.config.from_pyfile("conf.py")
    db.init_app(app)
    Session(app)

    # -- router --
    from .router import router
    router(app)

    # -- Create Database --
    if isfile("data.db"):
        with app.app_context():
            db.create_all(app=app)
            print("Created DB!")

    return app