from fastapi import FastAPI

import uvicorn

from src.app.views.routers.common_router import main_router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(main_router)
    return app


if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)
