from abc import ABC, abstractmethod
from typing import List, Optional

from src.core.entites import Category


class ICategoryReader(ABC):
    @abstractmethod
    def get_categories(self) -> List[Category]:
        pass

    @abstractmethod
    def get_categories_by_name(self, name: str) -> Optional[Category]:
        pass
