from typing import List
from fastapi import (
    FastAPI, 
    status, 
    Depends, 
    HTTPException
    )
from database.database import (
    SessionLocal,
    engine
    )
from schemas.user_auth import (
    UserAuth, 
    TokenSchema
    )
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from models.user import User
from models.task import Task
from models.transaction import Transaction
from user_deps import get_current_user
from utilities.password import (
    get_hashed_password,
    create_access_token,
    create_refresh_token,
    verify_password
    )

app = FastAPI(
    title="Manage Transactions Application",
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

@app.get("/manage")
def show_manage(db: Session = Depends(get_db)):
    records = db.query(Transaction).all()
    return records

@app.post('/signup', summary="Create new user", status_code=status.HTTP_200_OK)
async def create_user(data: UserAuth, db: Session = Depends(get_db)):
    records = db.query(User).filter(User.email ==data.email).all()
    
    if records !=[]:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist"
        )
    data = User(email= data.email,
                password= get_hashed_password(data.password),
                contact= data.contact)
    db.add(data)
    db.commit() 
    return {"msg":"Created Sucessfully"}


@app.post('/login', summary="Create access and refresh tokens for user", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    records = db.query(User).filter(User.email ==form_data.username).all()
    if records ==[]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    hashed_pass = records[0].password
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    
    return {
        "access_token": create_access_token(form_data.username),
        "refresh_token": create_refresh_token(form_data.username),
    }

@app.get('/me', summary='Get details of currently logged in user')
async def get_me(user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    records = db.query(User).filter(User.email==user).all()
    return {"email":records[0].email, "contact":records[0].contact}