from typing import List

from fastapi import APIRouter, Depends

from src.app.views.routers.schemas import CategoryResponse
from src.core.entites import Category
from src.core.usecases.category.get_categories import GetCategoriesUC, GetCategoriesDTO
from src.core.usecases.category.get_category_by_name import GetCategoriesIdUC, GetCategoriesIdDTO
from src.data.database import new_session
from src.data.repo.sqlA_category_repo import CategoryRepoBD

router = APIRouter()


@router.get('/{category_id}')
def get_category_by_name(category_id: int, db: Depends(new_session)) -> CategoryResponse:
    usecase = GetCategoriesIdUC(categories_repo=CategoryRepoBD(db))

    dto = GetCategoriesIdDTO(category_id=category_id)

    result = usecase.execute(dto=dto)
    return CategoryResponse(
        id=result.id,
        name=Category(result.name)
    )


@router.get('/')
def get_categories(db: Depends(new_session)) -> List[CategoryResponse]:
    usecase = GetCategoriesUC(categories_repo=CategoryRepoBD(db))
    dto = GetCategoriesDTO()
    result = usecase.execute(dto=dto)
    category_response = [
        CategoryResponse(
            id=result.id,
            name=Category(result.name)
        ) for product in result
    ]
    return category_response