class ProductException(Exception):
    pass


class NotFound(ProductException):
    pass


class Dublicate(ProductException):
    pass