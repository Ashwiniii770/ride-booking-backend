from fastapi import APIRouter
from models import Driver

router = APIRouter()

drivers = []

@router.post("/register-driver")
def register_driver(driver: Driver):
    drivers.append(driver.name)
    return {"message": f"Driver {driver.name} registered successfully"}