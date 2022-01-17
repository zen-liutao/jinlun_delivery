from .utils import JSONResponse
from .error import exception as exception_blueprint
from .auth import auth as auth_blueprint, login_manager
from .contract import contract as contract_blueprint
from .invoice import invoice as invoice_blueprint
from .product import product as product_blueprint


def init_app(app):
    app.response_class = JSONResponse
    app.register_blueprint(exception_blueprint, url_prefix='/error')
    app.register_blueprint(auth_blueprint, url_prefix="/")
    app.register_blueprint(contract_blueprint, url_prefix="/contract")
    app.register_blueprint(invoice_blueprint, url_prefix="/invoice")
    app.register_blueprint(product_blueprint, url_prefix="/product")
