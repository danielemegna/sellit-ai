import textwrap
from importlib.resources import files

from sellitai.categorizer.openai import OpenAIApiProductCategorizer


def main() -> None:
    print("============= Sell It AI =============")
    print("Detecting category for the product ....")

    categorizer = OpenAIApiProductCategorizer()
    category = categorizer.category_for(
        product_name="Macchina da caffè Magnifica Evo ECAM292.81.B EX:1",
        product_description= textwrap.dedent("""\
        Autenticità, innovazione e stile: Magnifica Evo è l’espressione perfetta dell’esperienza De’Longhi.
        Dal perfetto espresso all’italiana ad un’ampia selezione di bevande, tutto al solo tocco di un tasto:
        arricchisci ogni tazzina con una cremosa schiuma di latte grazie alla Tecnologia LatteCrema Hot e alla funzione MyLatte,
        pensata per ridurre gli sprechi. Puoi scegliere tra 7 bevande one-touch preimpostate tramite un'interfaccia facile da utilizzare.\
        """),
        available_categories=fetch_subito_categories(),
    )

    print(f"Category detected: {category}")
    print("Done.")
    print("======================================")


def fetch_subito_categories() -> str:
    return (
        files("sellitai.resources")
        .joinpath("subito-categories.md")
        .read_text(encoding="utf-8")
    )


if __name__ == "__main__":
    main()
