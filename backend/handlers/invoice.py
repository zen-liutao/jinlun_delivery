from flask import Blueprint, request
from sqlalchemy import or_

from backend.models import Invoice, db
from backend.serializers import InvoiceGetRequest, InvoiceCascadeSchema, InvoiceSchema, InvoicePutRequest, \
    InvoiceDelRequest

invoice = Blueprint('invoice', __name__)


@invoice.route("/", methods=["GET"])
def get():
    req = InvoiceGetRequest().load(request.get_json())

    invoices = Invoice.query.filter(
        or_(Invoice.id.in_(req.get("ids")), Invoice.no == req.get("no"), Invoice.tel == req.get("tel"))).paginate(
        req.get("page_number"), req.get("page_size"))

    if req.get("cascade"):
        invoices_data = InvoiceCascadeSchema().dump(invoices.items, many=True)
    else:
        invoices_data = InvoiceSchema().dump(invoices.items, many=True)

    res = {
        "total": invoices.total,
        "page_number": invoices.page,
        "page_size": invoices.per_page,
        "data": invoices_data
    }

    return res


@invoice.route("/", methods=["POST"])
def post():
    instance = InvoiceSchema().load(request.get_json())
    db.session.add(instance)
    return "ok"


@invoice.route("/", methods=["PUT", "PATCH"])
def put():
    partial = True if request.method == "PATCH" else False
    InvoicePutRequest().load(request.get_json(), partial=partial)
    return "ok"


@invoice.route("/", methods=["DELETE"])
def delete():
    req = InvoiceDelRequest().load(request.get_json())
    Invoice.query.filter(Invoice.id.in_(req.get("ids"))).delete(synchronize_session=False)
    return "ok"
