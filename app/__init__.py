import os
from flask import Flask
from flask_restful import Api
from app.resources.health import Health
from app.resources.user import User

def create_app():
    app = Flask(__name__)
    if 'FLASK_CONFIG' in os.environ.keys():
        app.config.from_object('app.settings.' + os.environ['FLASK_CONFIG'])
    else:
        app.config.from_object('app.settings.Development')

    # Init Flask-SQLALchemy
    from app.db import db
    db.init_app(app)


    # Routers
    api = Api(app)
    api.add_resource(Health, '/health')
    api.add_resource(User, '/user')
    return app