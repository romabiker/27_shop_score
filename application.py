import os


from flask import Flask


from extensions import db
from views import blueprint


def create_app():
    app = Flask(
        __name__.split('.')[0],
        static_url_path='/static',
    )
    app.config['SQLALCHEMY_DATABASE_URI'] =  os.environ.get(
                                             'SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.register_blueprint(blueprint)
    return app
