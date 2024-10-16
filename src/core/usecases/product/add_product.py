import dataclasses

from src.core.UnitOfWork import UnitOfWork
from src.core.entites import Product, Category
from src.core.usecase import IUseCase
from src.core.repo.i_proudct_repo import IProductsRepo
from src.core.usecases.product.product_service import ProductService


@dataclasses.dataclass
class AddProductDTO:
    name: str
    price: int
    сategory: Category


class AddNewProductUC(IUseCase):
    def __init__(self, product_repo: IProductsRepo, service: ProductService, uow: UnitOfWork):
        self.product_repo = product_repo
        self.service = service
        self.uow = uow

    def execute(self, dto: AddProductDTO) -> Product:
        new_product = self.service.create_product(name=dto.name, price=dto.price)
        new_product = self.product_repo.add_product(new_product)
        self.uow.commit()
        return new_product
