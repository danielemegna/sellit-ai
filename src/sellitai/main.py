from sellitai.categorizer.fake import FakeProductCategorizer


def main() -> None:
    print("============= Sell It AI =============")
    print("Detecting category for the product ....")

    categorizer = FakeProductCategorizer()
    category = categorizer.category_for(
        product_name="Wireless Mouse",
        product_description="A sleek wireless mouse with ergonomic design",
        available_categories=["Electronics", "Office Supplies", "Accessories"],
    )

    print(f"Category detected: {category}")
    print("Done.")


if __name__ == "__main__":
    main()