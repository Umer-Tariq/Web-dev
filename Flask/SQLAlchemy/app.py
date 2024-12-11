from models import db
from flask import Flask, Blueprint
from flask_migrate import Migrate
from views import views

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./testdb.db'

    db.init_app(app)

    app.register_blueprint(views, url_prefix = '/')

    Migrate(app, db)


    return app