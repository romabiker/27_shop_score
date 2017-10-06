from os import getenv


from flask import Flask


from extensions import db
from views import blueprint


def create_app():
    app = Flask(
        __name__.split('.')[0],
        static_url_path='/static',
    )
    app.config['SQLALCHEMY_DATABASE_URI'] =  getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DB_TIME_ZONE'] = getenv('DB_TIME_ZONE', 'Europe/Moscow')
    db.init_app(app)
    app.register_blueprint(blueprint)
    return app
