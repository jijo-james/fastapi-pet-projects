from fastapi import APIRouter

order_router = APIRouter(prefix="/orders", tags=["odrers"])


@order_router.get("/")
async def hello():
    return {"message": "Hello world"}
