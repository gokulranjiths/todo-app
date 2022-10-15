from sqlalchemy import String, Column, ForeignKey, Integer
from database.database import Base

class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    created_by = Column(Integer, ForeignKey("user_master.id"),nullable=False)
    name = Column(String, nullable=False)
