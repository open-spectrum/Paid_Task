from config import db
class Research(db.Model):
    id = db.Column(db.Integer,nullable=False,autoincrement=True,primary_key=True)
    task_name = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    task_pricing = db.Column(db.Float, nullable=False)
    questions = db.Column(db.JSON,nullable=False)
    img = db.Column(db.String(), nullable=True)
    def __repr__(self):
        return f'Research {self.task_name}'
