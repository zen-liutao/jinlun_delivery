from flask_migrate import MigrateCommand
from flask_script import Manager, Server

from backend import app

manager = Manager(app)

manager.add_command("db", MigrateCommand)
manager.add_command("runserver", Server(use_debugger=True))

if __name__ == '__main__':
    manager.run()
