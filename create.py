from config import db, app
from models.user_model import UserModel
from models.research_model import ResearchModel
from models.task_model import TaskModel
from models.task_history_model import TaskHistoryResearchModel

with app.app_context():
    db.create_all()
