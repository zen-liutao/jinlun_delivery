from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from backend.models import User, db


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True
        include_relationships = True
        load_instance = True
        sqla_session = db.session
        # fields = []
        # exclude = []
