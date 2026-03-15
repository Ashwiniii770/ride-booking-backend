from fastapi import APIRouter
from models import Rider

router = APIRouter()

riders = []

@router.post("/register-rider")
def register_rider(rider: Rider):
    riders.append(rider.name)
    return {"message": f"Rider {rider.name} registered successfully"}