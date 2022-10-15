from fastapi import FastAPI, status, Depends, HTTPException
from utilities.password import get_hased_password, verify_password
from database.database import SessionLocal, engine
from sqlalchemy.orm import Session
from models.task import Task
from typing import List

app = FastAPI(
    title="Todo Application",
    version="1.0"
)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"msg":"Hello World!!!"} 

@app.get("/records/")
def show_records(db: Session = Depends(get_db)):
    records = db.query(Task).all()
    return records