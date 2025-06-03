from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = 'rnzimblkhpp12342334465##'

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://paid_task:t@34.136.243.220//paid_task"

db = SQLAlchemy(app)

  
with app.app_context():
    db.create_all()
