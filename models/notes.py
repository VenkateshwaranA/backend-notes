from pydantic import BaseModel,  Field
from datetime import datetime

class User(BaseModel):
    email: str
    userName: str
    password: str
    # created_on: datetime = Field(default_factory=datetime.utcnow)
    # last_update: datetime = Field(default_factory=datetime.utcnow)

class Userlogin(BaseModel):
    email: str
    password: str

class Notes(BaseModel):
    user_id: str
    note_title: str
    note_content: str
    created_on: datetime = Field(default_factory=datetime.utcnow)
    last_update: datetime = Field(default_factory=datetime.utcnow)
