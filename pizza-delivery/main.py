from fastapi import FastAPI
from authentication_routes import auth_router
from order_routes import order_router
from fastapi_jwt_auth import AuthJWT
from schemas import Settings

app = FastAPI()


@AuthJWT.load_config
async def get_config():
    return Settings()

app.include_router(auth_router)
app.include_router(order_router)
