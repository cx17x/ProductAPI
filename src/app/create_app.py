from fastapi import FastAPI

from src.app.views.routers.common_router import router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
