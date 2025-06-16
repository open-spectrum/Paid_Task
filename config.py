from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import models

app = Flask(__name__)
app.secret_key = 'chavesupersecreta'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:root@localhost/paid_task?charset=utf8mb4"

db = SQLAlchemy(app)

