from fastapi import FastAPI, status, Depends, HTTPException
from utilities import get_hased_password, verify_password
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import schemas, models
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
    records = db.query(models.Task).all()
    return records