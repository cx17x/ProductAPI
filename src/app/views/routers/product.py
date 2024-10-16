from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.app.views.routers.schemas import ProductBase, ProductResponse, ProductFilterParams
from src.core.usecases.product.add_product import AddNewProductUC, AddProductDTO
from src.core.usecases.product.delete_product import DeleteProductUC, DeleteProductDTO
from src.core.usecases.product.get_product import GetProductUC, GetProductDTO
from src.core.usecases.product.get_products_filter import GetProductsFilterUC, GetProductsFilterDTO
from src.core.usecases.product.product_service import ProductService
from src.core.usecases.product.update_product import UpdateProductUC, UpdateProductDTO
from src.data.database import new_session
from src.data.repo.sqlA_product_repo import ProductRepoBD

router = APIRouter()


@router.get('/{product_id}')
def get_product(product_id: int, db: Depends(new_session)) -> ProductResponse:
    product_repo = ProductRepoBD(db)
    usecase = GetProductUC(product_repo=product_repo)
    dto = GetProductDTO(product_id=product_id)
    result = usecase.execute(dto=dto)
    return ProductResponse(
        name=result.name,
        price=result.price,
        category_id=result.category_id,
        id=result.id
    )


@router.post('/')
def add_product(product: ProductBase, db: Depends(new_session)) -> ProductResponse:
    product_repo = ProductRepoBD(db)
    usecase = AddNewProductUC(product_repo=product_repo, service=ProductService(), uow=db)
    dto = AddProductDTO(
        name=product.name,
        price=product.price,
        сategory=product.category
    )
    result = usecase.execute(dto=dto)
    return ProductResponse(
        name=result.name,
        price=result.price,
        category_id=result.category_id,
        id=result.id
    )


@router.put('/{product_id}')
def update_product(product_id: int, product: ProductBase, db: Depends(new_session)) -> ProductResponse:
    product_repo = ProductRepoBD(db)
    usecase = UpdateProductUC(product_repo=product_repo, service=ProductService(), uow=db)

    dto = UpdateProductDTO(
        product_id=product_id,
        name=product.name,
        price=product.price,
        category=product.category
    )
    result = usecase.execute(dto=dto)
    return ProductResponse(
        name=result.name,
        price=result.price,
        category_id=result.category_id,
        id=result.id
    )


@router.post('/filter')
def get_product_filter(filter_params: ProductFilterParams, db: Session = Depends(new_session)) -> List[ProductResponse]:
    usecase = GetProductsFilterUC(product_repo=ProductRepoBD(db))
    dto = GetProductsFilterDTO(
        category=filter_params.category,
        min_price=filter_params.min_price,
        max_price=filter_params.max_price
    )
    result = usecase.execute(dto=dto)
    products_response = [
        ProductResponse(
            id=product.id,
            name=product.name,
            price=product.price,
            category_id=product.category_id
        ) for product in result
    ]

    return products_response


@router.delete('/{product_id}')
def delete_product(product_id: int, db: Depends(new_session)) -> None:
    usecase = DeleteProductUC(product_repo=ProductRepoBD(db), uow=db)
    dto = DeleteProductDTO(
        product_id=product_id
    )
    usecase.execute(dto=dto)
