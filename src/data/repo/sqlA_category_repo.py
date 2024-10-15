from abc import ABC

from typing_extensions import Optional, List

from src.core.entites import Category
from src.core.repo.I_category_repo import ICategoryRepo


class CategoryRepoBD(ICategoryRepo):
    def get_categories(self) -> List[Category]:
        pass

    def get_categories_by_id(self, category_id: int) -> Optional[Category]:
        pass
