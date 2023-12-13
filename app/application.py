import os
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .health.health_check import router_health as health_check
from .routers.product_router import product_router


def create_application() -> FastAPI:
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=os.getenv("CORS_ORIGIN", []),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(health_check)
    app.include_router(product_router)

    return app
