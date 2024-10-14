from abc import ABC, abstractmethod
from typing import Optional, List

from src.core.entites import Product, Category


class IProductsRepo(ABC):
    @abstractmethod
    def add_product(self, product: Product) -> Product:
        pass

    @abstractmethod
    def delete_product(self, product_id: int) -> None:
        pass

    @abstractmethod
    def get_product(self, product_id: int) -> Product:
        pass

    @abstractmethod
    def update_product(self, product: Product, product_id: int) -> Product:
        pass

    @abstractmethod
    def get_product_filter(
            self,
            category: Optional[Category] = None,
            min_price: Optional[int] = None,
            max_price: Optional[int] = None
    ) -> List[Product]: pass

