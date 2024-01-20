import os
from flask import Flask
from dotenv import load_dotenv
from .models import db


load_dotenv()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
db.init_app(app)


from . import routes

