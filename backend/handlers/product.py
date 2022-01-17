from flask import Blueprint, request
from sqlalchemy import or_

from backend.models import Product, db
from backend.serializers import ProductGetRequest, ProductSchema, ProductPutRequest, ProductDelRequest

product = Blueprint('product', __name__)


@product.route("/", methods=["GET"])
def get():
    req = ProductGetRequest().load(request.get_json())

    contracts = Product.query.filter(
        or_(Product.id.in_(req.get("ids")), Product.product_name == req.get("product_name"),
            Product.serial_number == req.get("serial_number"))).paginate(req.get("page_number"), req.get("page_size"))

    res = {
        "total": contracts.total,
        "page_number": contracts.page,
        "page_size": contracts.per_page,
        "data": ProductSchema().dump(contracts.items, many=True)
    }
    return res


@product.route("/", methods=["POST"])
def post():
    instance = ProductSchema().load(request.get_json())
    db.session.add(instance)
    return "ok"


@product.route("/", methods=["PUT", "PATCH"])
def put():
    partial = True if request.method == "PATCH" else False
    ProductPutRequest().load(request.get_json(), partial=partial)
    return "ok"


@product.route("/", methods=["DELETE"])
def delete():
    req = ProductDelRequest().load(request.get_json())
    Product.query.filter(Product.id.in_(req.get("ids"))).delete(synchronize_session=False)
    return "ok"
