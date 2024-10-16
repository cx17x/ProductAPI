from abc import abstractmethod

from sqlalchemy.orm import Session, session, joinedload
from typing_extensions import Optional, List

from src.core.entites import Product, Category
from src.core.repo.exetentions import NotFound, AddingError
from src.core.repo.i_proudct_repo import IProductsRepo
from src.data.database import new_session
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
        product_model = self._entyty_to_model(product)
        self.db.add(product_model)

        return self._model_to_entity(product_model)

    def get_product(self, product_id: int) -> Optional[Product]:
        product_model = self.db.query(ProductModel).filter_by(id=product_id).first()
        if product_model:
            return self._model_to_entity(product_model)
        return NotFound

    def delete_product(self, product_id: int) -> None:
        product_model = self.db.query(ProductModel).filter_by(id=product_id).first()
        if product_model:
            self.db.delete(product_model)

    def update_product(self, product: Product, product_id: int) -> Optional[Product]:
        product_model = self.db.query(ProductModel).filter_by(id=product_id).first()
        if product_model:
            product_model.name = product.name
            product_model.price = product.price
            product_model.category_id = self.db.query(CategoryModel).filter_by(name=product.category_id).id

        return AddingError

    def get_product_filter(
            self,
            category: Optional[Category] = None,
            min_price: Optional[int] = None,
            max_price: Optional[int] = None
    ) -> List[Product]:
        query = self.db.query(ProductModel).options(joinedload(ProductModel.category))
        if category:
            query = query.filter(ProductModel.category.has(CategoryModel.name == category))
        if min_price:
            query = query.filter(ProductModel.price >= min_price)
        if max_price:
            query = query.filter(ProductModel.price >= max_price)
        products = query.all()
        return [self._model_to_entity(product) for product in products]

# repo = ProductRepoBD(next(new_session()))
#
# product = Product(id=None, name='Milk Product', price=100, category_id=1)
# product1 = Product(id=None, name='Milk213', price=30, category_id=1)
# product2 = Product(id=None, name='Milk 321', price=20, category_id=2)
# product3 = Product(id=None, name='Milk 43', price=50, category_id=2)
# product4 = Product(id=None, name='Milk 657', price=60, category_id=3)
#
# repo.add_product(product)
# repo.add_product(product1)
# repo.add_product(product2)
# repo.add_product(product3)
# repo.add_product(product4)
# print(repo.get_product(product_id=1))
# repo.delete_product(product_id=1)
#
# repo.get_product_filter(Category.MILK)
