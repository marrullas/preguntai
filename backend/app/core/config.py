import os

DATABASE_URL = os.environ.get("DATABASE_URL") or "sqlite:///./my_project.db"

SECRET_KEY = "PRUEBASDESECRET"