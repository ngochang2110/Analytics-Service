from fastapi import APIRouter

router_health = APIRouter(prefix="/health")


@router_health.get("/")
def health_check():
    return {"code": 200, "status": "Health check"}
