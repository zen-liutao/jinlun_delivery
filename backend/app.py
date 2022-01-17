from flask import Flask
from flask_migrate import Migrate


def create_app():
    from backend.models import db
    from backend import handlers
    from backend.handlers import login_manager
    app = Flask(__name__)

    app.config.from_object("backend.settings")

    migrate = Migrate()

    db.init_app(app)
    migrate.init_app(app, db)
    handlers.init_app(app)
    login_manager.init_app(app)

    return app
