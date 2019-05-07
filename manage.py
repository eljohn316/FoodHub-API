import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask import Flask
# from flask_cors import CORS

from app.main import create_app, db
from app.main.model import models
from app.main.model import blacklist
from app import blueprint

app = create_app('dev')
app.register_blueprint(blueprint)

app.app_context().push()

# CORS(app)

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
