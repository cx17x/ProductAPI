import dataclasses

from src.core.usecase import IUseCase
from src.core.repo.i_proudct_repo import IProductsRepo
from src.core.usecases.product.create_prod import ProductService


@dataclasses.dataclass
class DeleteProductDTO:
    product_id: int


class DeleteProductUC(IUseCase):
    def __int__(self, product_repo: IProductsRepo, service: ProductService):
        self.product_repo = product_repo


def execute(self, dto: DeleteProductDTO) -> None:
    delete_product = self.product_repo.delete_product(dto.product_id)
    return delete_product
