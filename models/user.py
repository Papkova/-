from sqlalchemy import Column, Integer, String
from .database import Base
from flask_login import UserMixin


class User(UserMixin, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(16))

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password