import os
import configparser
from sqlalchemy import create_engine
from sqlalchemy.orm import session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

config = configparser.ConfigParser()
config.read('config.ini')


SQLALCHEMY_DATABASE_URL = config.get('DB','DB_URL')

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()