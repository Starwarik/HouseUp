from fastapi import FastAPI, Form, Depends
from database_functions import *

app = FastAPI()

@app.post("/api/login")
def user_signin(user_name: str = Form(...), password: str = Form(...), session: Session = Depends(get_session)):
    user = get_user(session, user_name)
    if user:
        

