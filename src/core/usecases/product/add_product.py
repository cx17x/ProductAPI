import dataclasses

from src.core.entites import Product, Category
from src.core.usecase import IUseCase
from src.core.repo.i_proudct_repo import IProductsRepo
from src.core.usecases.product.create_prod import ProductService


@dataclasses.dataclass
class AddProductDTO:
    name: str
    price: int
    Category: Category


class AddNewProductUC(IUseCase):
    def __int__(self, product_repo: IProductsRepo, service: ProductService):
        self.product_repo = product_repo
        self.service = service

    def execute(self, dto: AddProductDTO) -> Product:
        new_product = self.service.create_product(name=dto.name, price=dto.price)
        new_product = self.product_repo.add_product(new_product)
        return new_product
