from marshmallow import fields, Schema, EXCLUDE
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

from backend.models import Contract, db
from .invoice import InvoiceCascadeSchema


class ContractSchema(SQLAlchemyAutoSchema):
    id = auto_field(dump_only=True)
    supplier = auto_field(required=True, error_messages={"required": "supplier are required"})
    buyer = auto_field(required=True, error_messages={"required": "buyer are required"})
    serial_number = auto_field(required=True, error_messages={"required": "serial_number are required"})
    address = auto_field()
    description = auto_field()
    create_at = auto_field(dump_only=True)
    update_at = auto_field(dump_only=True)

    class Meta:
        model = Contract
        # include_fk = True
        include_relationships = True
        load_instance = True
        sqla_session = db.session
        unknown = EXCLUDE
        # fields = []
        # exclude = []


class ContractCascadeSchema(ContractSchema):
    invoices = fields.List(fields.Nested(lambda: InvoiceCascadeSchema()))


class ContractGetRequest(Schema):
    ids = fields.List(fields.Integer(), load_default=[])
    supplier = fields.String(load_default="")
    buyer = fields.String(load_default="")
    serial_number = fields.String(load_default="")
    page_number = fields.Integer(load_default=1)
    page_size = fields.Integer(load_default=10)
    cascade = fields.Boolean(load_default=False)

    class Meta:
        unknown = EXCLUDE


class ContractPutRequest(ContractSchema):
    id = auto_field(required=True, error_messages={"required": "id are required"})


class ContractDelRequest(Schema):
    ids = fields.List(fields.Integer(), load_default=[])

    class Meta:
        unknown = EXCLUDE
