from marshmallow import fields, validate, Schema, EXCLUDE
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

from backend.models import Invoice, db
from .product import ProductSchema


class InvoiceSchema(SQLAlchemyAutoSchema):
    id = auto_field(dump_only=True)
    no = auto_field(required=True, error_messages={"required": "no are required"})
    tel = auto_field(required=True, validate=validate.Regexp("^1[3-9]\d{9}$", error="The phone number is incorrect"),
                     error_messages={"required": "Phone numbers are required"})
    address = auto_field()
    delivery_way = auto_field()
    description = auto_field()
    create_at = auto_field(dump_only=True)
    update_at = auto_field(dump_only=True)

    class Meta:
        model = Invoice
        include_fk = True
        include_relationships = True
        load_instance = True
        sqla_session = db.session
        unknown = EXCLUDE
        # fields = []
        # exclude = []


class InvoiceCascadeSchema(InvoiceSchema):
    products = fields.List(fields.Nested(lambda: ProductSchema()))


class InvoiceGetRequest(Schema):
    ids = fields.List(fields.Integer(), load_default=[])
    no = fields.String(load_default="")
    tel = fields.String(load_default="")
    page_number = fields.Integer(load_default=1)
    page_size = fields.Integer(load_default=10)
    cascade = fields.Boolean(load_default=False)

    class Meta:
        unknown = EXCLUDE


class InvoicePutRequest(InvoiceSchema):
    id = auto_field(required=True, error_messages={"required": "id are required"})


class InvoiceDelRequest(Schema):
    ids = fields.List(fields.Integer(), load_default=[])

    class Meta:
        unknown = EXCLUDE
