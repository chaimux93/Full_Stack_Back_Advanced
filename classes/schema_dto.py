from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str

class UserNoID(BaseModel):
    username: str
    email: str

class Project(BaseModel):
    id: int
    name: str
    description: str

class ProjectNoID(BaseModel):
    name: str
    description: str
