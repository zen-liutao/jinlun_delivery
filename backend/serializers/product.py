from marshmallow import fields, EXCLUDE, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

from backend.models import Product, db


class ProductSchema(SQLAlchemyAutoSchema):
    id = auto_field(dump_only=True)
    serial_number = auto_field(unique=True)
    product_name = auto_field()
    specification = auto_field()
    material = auto_field()
    drawing_number = auto_field()
    unit = auto_field()
    quantity = auto_field()
    unit_price = auto_field()
    type = auto_field()
    remark = auto_field()
    description = auto_field()
    create_at = auto_field(dump_only=True)
    update_at = auto_field(dump_only=True)

    class Meta:
        model = Product
        include_fk = True
        # include_relationships = True
        load_instance = True
        sqla_session = db.session
        unknown = EXCLUDE
        # fields = []
        # exclude = []


class ProductGetRequest(Schema):
    ids = fields.List(fields.Integer(), load_default=[])
    product_name = fields.String(load_default="")
    serial_number = fields.String(load_default="")
    page_number = fields.Integer(load_default=1)
    page_size = fields.Integer(load_default=10)

    class Meta:
        unknown = EXCLUDE


class ProductPutRequest(ProductSchema):
    id = auto_field(required=True, error_messages={"required": "id are required"})


class ProductDelRequest(Schema):
    ids = fields.List(fields.Integer(), load_default=[])

    class Meta:
        unknown = EXCLUDE
