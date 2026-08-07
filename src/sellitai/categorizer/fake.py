from sellitai.categorizer.ecommerce import Ecommerce
from sellitai.categorizer.interfaces import ProductCategorizer


class FakeProductCategorizer(ProductCategorizer):

    def category_for(
        self,
        product_name: str,
        product_description: str,
        ecommerce: Ecommerce,
    ) -> str:
        return "Elettronica -> Informatica"