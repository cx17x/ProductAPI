import dataclasses
from typing import Optional, List

from src.core.entites import Product, Category
from src.core.usecase import IUseCase
from src.core.repo.i_proudct_repo import IProductsRepo


@dataclasses.dataclass
class GetProductsFilterDTO:
    category: Optional[Category] = None,
    min_price: Optional[int] = None,
    max_price: Optional[int] = None


class GetProductsFilterUC(IUseCase):
    def __int__(self, product_repo: IProductsRepo):
        self.product_repo = product_repo


def execute(self, dto: GetProductsFilterDTO) -> List[Product]:
    return self.product_repo.get_product_filter(
        category=dto.category,
        min_price=dto.min_price,
        max_price=dto.max_price
    )
