import dataclasses
from enum import Enum
from typing import Optional


class Category(Enum):
    MILK = 'milk'
    BREAD = 'bread'
    FRUIT = 'fruit'


@dataclasses.dataclass
class CategoryType:
    name: Category
    id: Optional[int] = None


@dataclasses.dataclass
class Product:
    name: str
    price: int
    category_id: int
    id: Optional[int] = None
