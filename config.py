from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = 'rnzimblkhpp12342334465##'

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:root@localhost/paid_task?charset=utf8mb4"


db = SQLAlchemy(app)

  
with app.app_context():
    db.create_all()
