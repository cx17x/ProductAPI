import dataclasses

from src.core.UnitOfWork import UnitOfWork
from src.core.entites import Product, Category
from src.core.usecase import IUseCase
from src.core.repo.i_proudct_repo import IProductsRepo
from src.core.usecases.product.product_service import ProductService


@dataclasses.dataclass
class UpdateProductDTO:
    product_id: int
    name: str
    price: int
    category: Category


class UpdateProductUC(IUseCase):
    def __init__(self, product_repo: IProductsRepo, service: ProductService, uow: UnitOfWork):
        self.product_repo = product_repo
        self.service = service
        self.uow = uow

    def execute(self, dto: UpdateProductDTO) -> Product:
        curr_product = self.product_repo.get_product(dto.product_id)

        updated_product = self.service.update_product(
            product=curr_product,
            name=dto.name,
            price=dto.price,
            category=dto.category

        )

        updated_product = self.product_repo.update_product(updated_product)
        self.uow.commit()
        return updated_product
