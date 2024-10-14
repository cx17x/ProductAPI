import dataclasses
from enum import Enum
from typing import Optional


class Category(Enum):
    MILK = 'milk'
    BREAD = 'bread'
    FRUIT = 'fruit'


@dataclasses.dataclass
class Product:
    name: str
    price: int
    category: Category
    id: Optional[int] = None
