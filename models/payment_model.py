from config import db
from datetime import datetime

class Payment(db.Model):
    __tablename__ = 'payments'


    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    status = db.Column(db.String(45), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    id_user = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    pix_key = db.Column(db.String(255),nullable=False)

    def __repr__(self):
        return f'<Payment {self.id} - Status: {self.status} - R${self.quantity:.2f}>'