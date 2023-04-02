from sqlalchemy.orm import Session
from fastapi_users.db import SQLAlchemyBaseUserTable
from app.models.users import User
from app.core.config import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserTable(User, SQLAlchemyBaseUserTable):
    pass
