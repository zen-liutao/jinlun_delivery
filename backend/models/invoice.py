from .base import Base, db


class Invoice(Base):
    __tablename__ = "invoice"

    no = db.Column(db.String(20), unique=True)
    tel = db.Column(db.String(20))
    address = db.Column(db.String(60))
    delivery_way = db.Column(db.String(60))
    description = db.Column(db.Text)

    contract_id = db.Column(db.Integer, db.ForeignKey("contract.id"))
    products = db.relationship("Product", backref="invoice", lazy=True)

    def __repr__(self):
        return "no: %s, address: %s, delivery_way: %s" % (self.no, self.address, self.delivery_way)
