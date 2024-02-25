import os
from flask import Flask
from flask_caching import Cache
from datetime import timedelta
from dotenv import load_dotenv
from .models import database
from flask_login import LoginManager

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(os.getcwd())}/app.sqlite3"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=10)

# Ініціалізація кешу
cache = Cache(app, config={"CACHE_TYPE": "SimpleCache"})

database.__init__(app)

from . import routes
