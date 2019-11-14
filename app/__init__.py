#$ FLASK_APP=microblog.py FLASK_DEBUG=1 python -m flask run

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_redis import FlaskRedis
from flask import render_template, flash, redirect, url_for


db = SQLAlchemy()

def create_app():
    print('=====>> creating app <<=====')
    app = Flask(__name__)
    app.config.from_object(Config)

    with app.app_context():
        db.init_app(app)  

        from .stock_monitor import create_module as sm_create_module
        sm_create_module(app)

        return app
    