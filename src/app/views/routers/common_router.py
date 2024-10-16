from fastapi import APIRouter

from src.app.views.routers import category, product

router = APIRouter()

router.include_router(
    category.router,
    prefix='categoires'
)

router.include_router(
    product.router,
    prefix='products'
)