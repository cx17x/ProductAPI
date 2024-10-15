import dataclasses

from src.core.entites import Product
from src.core.usecase import IUseCase
from src.core.repo.i_proudct_repo import IProductsRepo


@dataclasses.dataclass
class GetProductDTO:
    product_id: int


class GetProductUC(IUseCase):
    def __init__(self, product_repo: IProductsRepo):
        self.product_repo = product_repo

    def execute(self, dto: GetProductDTO) -> Product:
        get_product = self.product_repo.get_product(dto.product_id)
        return get_product
