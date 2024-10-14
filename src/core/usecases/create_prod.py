from src.core.entites import Product, Category


class ProductService:
    def create_product(self, name: str, price: int, category: Category) -> Product:
        product = Product(
            name=name,
            price=price,
            id=None,
            category=category
        )

        return product

    def update_product(self, product: Product, name: str, price: int, category: Category) -> Product:
        product.name = name
        product.price = price
        product.category = category

        return product
