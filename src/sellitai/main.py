from flask import Flask, Response, request

from sellitai.categorizer.ecommerce import Ecommerce
from sellitai.categorizer.interfaces import ProductCategorizer
from sellitai.categorizer.openai import OpenAIApiProductCategorizer

app = Flask(__name__)


@app.post("/categorize")
def categorize() -> Response:
    body = request.get_json()

    try:
        ecommerce = Ecommerce(body["categories"])
    except (KeyError, ValueError):
        return Response(
            'Invalid "categories" field. Allowed values: SUBITO, VINTED.',
            status=400,
            mimetype="text/plain",
        )

    categorizer: ProductCategorizer = OpenAIApiProductCategorizer()
    category = categorizer.category_for(
        product_name=body["product_name"],
        product_description=body["product_description"],
        ecommerce=ecommerce,
    )

    return Response(category, mimetype="text/plain")


def main() -> None:
    app.run(host="0.0.0.0", port=8001)


if __name__ == "__main__":
    main()
