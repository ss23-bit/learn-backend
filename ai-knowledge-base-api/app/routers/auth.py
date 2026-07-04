from fastapi import APIRouter
from app.schema import UserCreate
router = APIRouter(prefix="auth", tags=["Auth"])

@router.post("/register")
def register(user: UserCreate)