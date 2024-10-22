from abc import ABC

from sqlalchemy.orm import Session
from typing_extensions import Optional, List

from src.core.entites import Category, CategoryType
from src.core.repo.I_category_repo import ICategoryRepo
from src.data.model import CategoryModel


class CategoryRepoBD(ICategoryRepo):

    def __init__(self, db_session: Session):
        self.db = db_session

    def _model_to_entity(self, category: CategoryModel):
        return CategoryType(
            name=category.name,
            id=category.id
        )

    def _entyty_to_model(self, category_entity: CategoryType):
        return CategoryModel(
            name=category_entity.name,
            id=category_entity.id
        )

    def get_categories(self) -> List[CategoryType]:
        categories = self.db.query(CategoryModel).all()
        return [self._model_to_entity(category) for category in categories]

    def get_categories_by_id(self, category_id: int) -> Optional[CategoryType]:
        category = self.db.query(CategoryModel).get(category_id)
        if category:
            return self._model_to_entity(category)
        return None
