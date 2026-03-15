from database import engine
from db_models import Base

Base.metadata.create_all(bind=engine)


from database import engine
import db_models

db_models.Base.metadata.create_all(bind=engine)


from fastapi import FastAPI
import riders
import drivers
import rides

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Ride Booking Backend"}

app.include_router(riders.router)
app.include_router(drivers.router)
app.include_router(rides.router)