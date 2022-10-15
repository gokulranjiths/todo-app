from sqlalchemy import String, Column, ForeignKey, Float, Integer
from database.database import Base

class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    user_id= Column(Integer, ForeignKey("user_master.id"),nullable=False)
    type_= Column(String, nullable=False)
    mode= Column(String, nullable=False )
    amount= Column(Float, nullable=False)
    project_id=Column(Integer, ForeignKey("project.id"),nullable=False)
    category= Column(String, nullable=False )
