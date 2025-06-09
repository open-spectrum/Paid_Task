from config import db

class Ads(db.Model):
    id = db.Column(db.Integer,nullable=False,primary_key=True,autoincrement=True,unique=True)
    content = db.Column(db.Text,nullable=False)
    type_ad = db.Column(db.String(255),nullable=False)

    def __repr__(self):
        return f" Id In Db: {id.self}"