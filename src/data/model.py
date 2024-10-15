from sqlalchemy import MetaData, Column, Integer, String, Enum as SqlEnum, ForeignKey
from sqlalchemy.orm import relationship

from src.core.entites import Category
from src.data.database import Base


class CategoryModel(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(SqlEnum(Category), nullable=False, unique=True)

    # products = relationship('ProductModel)ProductModel


class ProductModel(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    category = relationship(CategoryModel)
