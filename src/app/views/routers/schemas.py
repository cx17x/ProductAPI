from typing import Optional

from pydantic import BaseModel

from src.core.entites import Category


class ProductBase(BaseModel):
    name: str
    price: int
    category: Category


class ProductCreate(ProductBase):
    pass


class ProductFilterParams(BaseModel):
    category: Optional[Category] = None
    min_price: Optional[int] = None
    max_price: Optional[int] = None


class ProductResponse(ProductBase):
    name: str
    price: int
    category_id: int
    id: int


class CategoryResponse(BaseModel):
    id: int
    name: Category