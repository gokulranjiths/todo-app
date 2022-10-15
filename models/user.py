from sqlalchemy import String, Column, Integer
from database.database import Base

class User(Base):
    __tablename__ = "user_master"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column(String, nullable=False)
    contact = Column(String, nullable=False)
    email = Column(String, nullable=False)
