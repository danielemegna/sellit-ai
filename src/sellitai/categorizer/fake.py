from sellitai.categorizer.interfaces import ProductCategorizer


class FakeProductCategorizer(ProductCategorizer):

    def category_for(
        self,
        product_name: str,
        product_description: str,
        available_categories: str,
    ) -> str:
        return "Elettronica -> Informatica"