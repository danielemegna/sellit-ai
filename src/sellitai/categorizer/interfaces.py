from abc import ABC, abstractmethod


class ProductCategorizer(ABC):

    @abstractmethod
    def category_for(
        self,
        product_name: str,
        product_description: str,
        available_categories: list[str],
    ) -> str:
        ...