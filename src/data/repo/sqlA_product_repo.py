from abc import abstractmethod

from sqlalchemy.orm import Session
from typing_extensions import Optional, List

from src.core.entites import Product, Category
from src.core.repo.exetentions import NotFound
from src.core.repo.i_proudct_repo import IProductsRepo
from src.data.model import ProductModel, CategoryModel


class ProductRepoBD(IProductsRepo):
    def __init__(self, db_session: Session):
        self.db = db_session

    def _model_to_entity(self, product: ProductModel):
        return Product(
            id=product.id,
            name=product.name,
            price=product.price,
            category_id=product.category_id
        )

    def _entyty_to_model(self, product_entity: Product):
        return ProductModel(
            id=product_entity.id,
            name=product_entity.name,
            price=product_entity.price,
            category_id=product_entity.category_id
        )

    def add_product(self, product: Product) -> Product:
        category = self.db.query(CategoryModel).filter_by(name=product.category_id).first()
        if not category:
            raise NotFound
        product_model = self._entyty_to_model(product)
        self.db.add(product_model)
        self.db.commit()

        return self._model_to_entity(product_model)

    def get_product(self, product_id: int) -> Product:
        pass

    def delete_product(self, product_id: int) -> None:
        pass

    def update_product(self, product: Product, product_id: int) -> Product:
        pass

    def get_product_filter(
            self,
            category: Optional[Category] = None,
            min_price: Optional[int] = None,
            max_price: Optional[int] = None
    ) -> List[Product]:
        pass
