from fastapi import APIRouter

from src.app.views.routers import category, product

main_router = APIRouter()

main_router.include_router(
    category.category_router,
    prefix='/categoires'
)

main_router.include_router(
    product.product_router,
    prefix='/products'
)