from flask_login import UserMixin
from .base import Base, db


class User(Base, UserMixin):
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
