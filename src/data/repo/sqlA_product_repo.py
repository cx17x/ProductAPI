from sqlalchemy.orm import Session

from src.core.entites import Product, Category
from src.core.repo.I_service_repo import ICategoryReader
from src.core.repo.i_proudct_repo import IProductsRepo
from src.data.model import ProductModel, CategoryModel


class ProductRepoBD(IProductsRepo):
    def __init__(self, db_session: Session):
        self.db = db_session

    def _model_to_entyty(self, product: ProductModel, ):
        return Product(
            id=product.id,
            name=product.name,
            price=product.price,
            category=CategoryModel(
                id=product.category.id,
                name=product.category.name
            )
        )

    def entyty_to_model(self, product_entyty: Product):
        category = Category(
            id=product_entyty.category.id,
            name=product_entyty.category.name
        )
        return ProductModel(
            id = product_entyty.id,
            name = product_entyty.name,
            price = product_entyty.price,
            category = product_entyty.category
        )

class ProductRepoBD(ICategoryReader):
    pass