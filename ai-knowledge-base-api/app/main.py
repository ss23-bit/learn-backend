from fastapi import FastAPI
from app.routers import users

# intialize models relationship
import app.models

app = FastAPI()

app.include_router(users.router)
