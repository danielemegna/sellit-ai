from abc import ABC, abstractmethod

from sellitai.categorizer.ecommerce import Ecommerce


class ProductCategorizer(ABC):

    @abstractmethod
    def category_for(
        self,
        product_name: str,
        product_description: str,
        ecommerce: Ecommerce,
    ) -> str:
        ...