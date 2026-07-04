from fastapi import APIRouter
from app.schema import CreateUser

router = APIRouter(prefix="users", tags=["Users"])


@router.post("/")
def create_user(user: CreateUser):
    