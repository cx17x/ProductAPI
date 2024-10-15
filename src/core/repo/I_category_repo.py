from abc import ABC, abstractmethod
from typing import List, Optional

from src.core.entites import Category


class ICategoryRepo(ABC):
    @abstractmethod
    def get_categories(self) -> List[Category]:
        pass

    @abstractmethod
    def get_categories_by_id(self, category_id: int) -> Optional[Category]:
        pass
