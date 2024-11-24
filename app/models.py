from pydantic import BaseModel

class User(BaseModel):
    name: str
    password: str

class UserDevice(BaseModel):
    id: int
    user_name: str
    name: str
    type: str
    settings: str

class UserScenario(BaseModel):
    id: int
    user_name: str
    name: str
    content: str