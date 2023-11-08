# main.py
from fastapi import FastAPI
from router import routers_user  
from router import routers_projet  

app = FastAPI(
    title="Project Management API"
)

app.include_router(router_user, prefix="/users", tags=["Users"])
app.include_router(router_projet, prefix="/projects", tags=["Projects"])
