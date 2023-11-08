# router_projet.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Project(BaseModel):
    id: str
    name: str
    description: str

projects = []

@router_projet.post('/projects', response_model=Project, status_code=201)
async def create_project(project: Project):
    projects.append(project)
    return project

@router_projet.get('/projects', response_model=List[Project])
async def get_projects():
    return projects

@router_projet.get('/projects/{project_id}', response_model=Project)
async def get_project(project_id: str):
    for project in projects:
        if project.id == project_id:
            return project
    raise HTTPException(status_code=404, detail="Project not found")

@router_projet.put('/projects/{project_id}', response_model=Project)
async def update_project(project_id: str, updated_project: Project):
    for project in projects:
        if project.id == project_id:
            project.name = updated_project.name
            project.description = updated_project.description
            return project
    raise HTTPException(status_code=404, detail="Project not found")

@router_projet.delete('/projects/{project_id}', status_code=204)
async def delete_project(project_id: str):
    for project in projects:
        if project.id == project_id:
            projects.remove(project)
            return
    raise HTTPException(status_code=404, detail="Project not found")
