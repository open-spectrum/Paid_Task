from config import db, app
from models.user_model import Users
from models.research_model import Research
from models.ads_model import Ads
from models.payment_model import Payment
from models.task_history_model import TaskHistoryResearch

with app.app_context():
  
    db.create_all()
    #cria admin
    #user_admin = Users(username="spectra",password="spectramin",sald=0,roleId=1)
    #db.session.add(user_admin)
    #db.session.commit()
    print("Successo! Tabelas Criada.")
