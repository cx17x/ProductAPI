import dataclasses

from typing_extensions import List

from src.core.entites import Category
from src.core.repo.I_category_repo import ICategoryRepo
from src.core.usecase import IUseCase


@dataclasses.dataclass
class GetCategoriesDTO:
    pass


class GetCategoriesUC(IUseCase):
    def __init__(self, categories_repo: ICategoryRepo):
        self.categories_repo = categories_repo

    def execute(self, dto: GetCategoriesDTO) -> List[Category]:
        get_categories = self.categories_repo.get_categories()
        return get_categories
