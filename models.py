from pydantic import BaseModel

class Rider(BaseModel):
    name: str

class Driver(BaseModel):
    name: str

class RideRequest(BaseModel):
    rider_name: str