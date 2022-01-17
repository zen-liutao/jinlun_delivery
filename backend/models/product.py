from .base import Base, db


class Product(Base):
    __tablename__ = "product"

    serial_number = db.Column(db.String(120), unique=True)
    product_name = db.Column(db.String(120), index=True)
    specification = db.Column(db.String(120))
    material = db.Column(db.String(120))
    drawing_number = db.Column(db.String(120))
    unit = db.Column(db.String(120))
    quantity = db.Column(db.Integer)
    unit_price = db.Column(db.BigInteger)
    type = db.Column(db.SmallInteger)
    remark = db.Column(db.String(120))
    description = db.Column(db.Text)

    contract_id = db.Column(db.Integer, db.ForeignKey("contract.id"))
    invoice_id = db.Column(db.Integer, db.ForeignKey("invoice.id"))

    def __repr__(self):
        return "serial_number: %s, product_name: %s" % (self.serial_number, self.product_name)
