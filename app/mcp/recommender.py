from fastapi import APIRouter

router = APIRouter()

# Hardcoded for example
itinerary_templates = {
    2: "Phuket-Krabi Highlights",
    3: "Phuket Full Tour",
    5: "Phuket + Krabi + Island hopping",
    8: "Thailand Grand Tour"
}

@router.get("/recommend")
def recommend_itinerary(nights: int):
    recommendation = itinerary_templates.get(nights, "No recommended itinerary found")
    return {"nights": nights, "recommendation": recommendation}
