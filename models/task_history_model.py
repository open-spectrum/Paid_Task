from datetime import datetime
from config import db

from sqlalchemy.dialects.mysql import INTEGER

class TaskHistoryResearch(db.Model):
    __tablename__ = "task_history_research"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # id_user referente a users.id que é int (signed)
    id_user = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # id_research referente a research.id que é int unsigned
    id_research = db.Column(INTEGER(unsigned=True), db.ForeignKey("research.id"), nullable=False)

    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<TaskHistory {self.id}>"
