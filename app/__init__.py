from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///market.db'
app.config["SECRET_KEY"] = "3c5c9bb69735b9677e917d5d"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from app import routes