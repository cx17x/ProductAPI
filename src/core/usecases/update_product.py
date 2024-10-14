import dataclasses

from src.core.entites import Product, Category
from src.core.usecase import IUseCase
from src.core.repo.i_proudct_repo import IProductsRepo
from src.core.usecases.create_prod import ProductService


@dataclasses.dataclass
class UpdateProductDTO:
    product_id: int
    name: str
    price: int
    category: Category


class UpdateProductUC(IUseCase):
    def __int__(self, product_repo: IProductsRepo, service: ProductService):
        self.product_repo = product_repo
        self.service = service

    def execute(self, dto: UpdateProductDTO) -> Product:
        curr_product = self.product_repo.get_product(dto.product_id)

        updated_product = self.service.update_product(
            product=curr_product,
            name=dto.name,
            price=dto.price,
            category=dto.category

        )

        updated_product = self.product_repo.update_product(updated_product)

        return updated_product
