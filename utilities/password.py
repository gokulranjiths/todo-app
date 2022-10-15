from passlib.context import CryptContext

pwd_crpt=CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hased_password(plain_password):
    return pwd_crpt.hash(plain_password)

def verify_password(plain_password, hashed_password):
    return pwd_crpt.verify(plain_password, hashed_password)