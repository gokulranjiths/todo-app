from sqlalchemy import String, Column
from database import Base

class Task(Base):
    __tablename__ = "task"

    id = Column(String, primary_key=True, index=True, nullable=False)
    text = Column(String, index=True, nullable=False)
