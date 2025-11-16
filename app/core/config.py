import os
from dotenv import load_dotenv

environment = os.getenv("ENVIRONMENT", "dev")

if environment == "prod":
    load_dotenv(".env.prod")
elif environment == "dev":
    load_dotenv(".env.dev")
else:
    load_dotenv(".env.dev")

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))