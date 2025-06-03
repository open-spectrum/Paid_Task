
from config import db

class Users(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.String(45),unique=True,nullable=False)
    password = db.Column(db.String(65),nullable=False)
    sald = db.Column(db.Float,nullable=False)
    pix_key =db.Column(db.String(255),nullable=True)
    roleId = db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"