from fastapi import FastAPI, status
from utilities import get_hased_password, verify_password

app = FastAPI(
    title="Social Media Feed",
    version="1.0"
)

@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"msg":"Hello World!!!"} 