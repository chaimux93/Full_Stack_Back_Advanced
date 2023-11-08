# router_user.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class User(BaseModel):
    id: str
    name: str

users = []

@router_user.post('/users', response_model=User, status_code=201)
async def create_user(user: User):
    users.append(user)
    return user

@router_user.get('/users', response_model=List[User])
async def get_users():
    return users

@router_user.get('/users/{user_id}', response_model=User)
async def get_user(user_id: str):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router_user.put('/users/{user_id}', response_model=User)
async def update_user(user_id: str, updated_user: User):
    for user in users:
        if user.id == user_id:
            user.name = updated_user.name
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router_user.delete('/users/{user_id}', status_code=204)
async def delete_user(user_id: str):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return
    raise HTTPException(status_code=404, detail="User not found")
