from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from routes import friend_blueprint
from models import db


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./friends.db'
    CORS(app)

    db.init_app(app)

    app.register_blueprint(friend_blueprint)

    Migrate(app, db)

    return app
