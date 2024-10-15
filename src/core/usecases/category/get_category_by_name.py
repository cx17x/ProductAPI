import dataclasses

from typing_extensions import Optional

from src.core.entites import Category
from src.core.repo.I_category_repo import ICategoryRepo
from src.core.usecase import IUseCase


@dataclasses.dataclass
class GetCategoriesIdDTO:
    category_id: int


class GetCategoriesIdUC(IUseCase):
    def __init__(self, categories_repo: ICategoryRepo):
        self.categories_repo = categories_repo

    def execute(self, dto: GetCategoriesIdDTO) -> Optional[Category]:
        get_categories = self.categories_repo.get_categories_by_id(dto.category_id)
        return get_categories
