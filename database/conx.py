import sqlalchemy
from dotenv import load_dotenv, find_dotenv
import os
from os.path import join, dirname
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)


from dotenv import load_dotenv, find_dotenv

SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://" + os.getenv('DB_USERNAME') + ":" + os.getenv('DB_PASSWORD') + "@" + os.getenv('DB_HOST') + ":3306/" + os.getenv('DB_NAME')
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


