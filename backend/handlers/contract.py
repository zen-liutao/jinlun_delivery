from flask import Blueprint, request
from sqlalchemy import or_

from backend.models import Contract, db
from backend.serializers import ContractSchema, ContractGetRequest, ContractDelRequest, ContractPutRequest, \
    ContractCascadeSchema

contract = Blueprint('contract', __name__)


@contract.route("/", methods=["GET"])
def get():
    req = ContractGetRequest().load(request.get_json())

    contracts = Contract.query.filter(or_(Contract.id.in_(req.get("ids")), Contract.supplier == req.get("supplier"),
                                          Contract.buyer == req.get("buyer"),
                                          Contract.serial_number == req.get("serial_number"))).paginate(
        req.get("page_number"), req.get("page_size"))

    if req.get("cascade"):
        contracts_data = ContractCascadeSchema().dump(contracts.items, many=True)
    else:
        contracts_data = ContractSchema().dump(contracts.items, many=True)

    res = {
        "total": contracts.total,
        "page_number": contracts.page,
        "page_size": contracts.per_page,
        "data": contracts_data
    }

    return res


@contract.route("/", methods=["POST"])
def post():
    instance = ContractSchema().load(request.get_json())
    db.session.add(instance)
    return "ok"


@contract.route("/", methods=["PUT", "PATCH"])
def put():
    partial = True if request.method == "PATCH" else False
    ContractPutRequest().load(request.get_json(), partial=partial)
    return "ok"


@contract.route("/", methods=["DELETE"])
def delete():
    req = ContractDelRequest().load(request.get_json())
    Contract.query.filter(Contract.id.in_(req.get("ids"))).delete(synchronize_session=False)
    return "ok"
