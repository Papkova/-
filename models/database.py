from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database = create_engine("sqlite:///app.db", connect_args={"check_same_thread": False})
Session = sessionmaker(bind=database)
session = Session()  # Створюємо сесію щоб там все зберігати
Base = declarative_base()  # наслідування в базі даних


def create_db():
    Base.metadata.create_all(database)  # створює всі таблиці в базі даних
