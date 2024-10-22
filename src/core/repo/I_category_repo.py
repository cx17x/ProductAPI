from abc import ABC, abstractmethod
from typing import List, Optional

from src.core.entites import Category, CategoryType


class ICategoryRepo(ABC):
    @abstractmethod
    def get_categories(self) -> List[CategoryType]:
        pass

    @abstractmethod
    def get_categories_by_id(self, category_id: int) -> Optional[CategoryType]:
        pass
