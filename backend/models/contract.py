from .base import Base, db


class Contract(Base):
    __tablename__ = "contract"

    supplier = db.Column(db.String(120))
    buyer = db.Column(db.String(120))
    serial_number = db.Column(db.String(60), unique=True)
    address = db.Column(db.String(120))
    description = db.Column(db.Text)

    invoices = db.relationship("Invoice", backref="contract", lazy=True)

    def __repr__(self):
        return "serial_number: %s, supplier: %s, buyer: %s" % (self.serial_number, self.supplier, self.buyer)
