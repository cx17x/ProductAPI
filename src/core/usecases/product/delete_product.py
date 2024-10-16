import dataclasses

from src.core.UnitOfWork import UnitOfWork
from src.core.usecase import IUseCase
from src.core.repo.i_proudct_repo import IProductsRepo
from src.core.usecases.product.product_service import ProductService


@dataclasses.dataclass
class DeleteProductDTO:
    product_id: int


class DeleteProductUC(IUseCase):
    def __init__(self, product_repo: IProductsRepo, uow: UnitOfWork):
        self.product_repo = product_repo
        self.uow = uow

    def execute(self, dto: DeleteProductDTO) -> None:
        delete_product = self.product_repo.delete_product(dto.product_id)
        self.uow.commit()
        return delete_product
