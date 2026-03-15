from fastapi import APIRouter

router = APIRouter()

rides = []


@router.get("/rides")
def get_rides():
    return rides


@router.put("/ride-status/{ride_id}")
def update_ride_status(ride_id: int, status: str):
    if ride_id >= len(rides):
        return {"error": "Ride not found"}

    rides[ride_id]["status"] = status
    return {"message": "Ride status updated", "ride": rides[ride_id]}


@router.delete("/ride/{ride_id}")
def cancel_ride(ride_id: int):
    if ride_id >= len(rides):
        return {"error": "Ride not found"}

    cancelled = rides.pop(ride_id)

    return {
        "message": "Ride cancelled",
        "ride": cancelled
    }