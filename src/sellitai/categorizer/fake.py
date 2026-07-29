from sellitai.categorizer.interfaces import ProductCategorizer


class FakeProductCategorizer(ProductCategorizer):

    def category_for(
        self,
        product_name: str,
        product_description: str,
        available_categories: list[str],
    ) -> str:
        return available_categories[0] if available_categories else ""