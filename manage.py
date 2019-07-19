from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from run import create_app
from app.db import db

from app.models.user import UserModel

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()