import textwrap
from importlib.resources import files

from openai import OpenAI
from openai.types.chat import ChatCompletionUserMessageParam

from sellitai.categorizer.ecommerce import Ecommerce
from sellitai.categorizer.interfaces import ProductCategorizer


class OpenAIApiProductCategorizer(ProductCategorizer):

    def category_for(
        self,
        product_name: str,
        product_description: str,
        ecommerce: Ecommerce,
    ) -> str:

        match ecommerce:
            case Ecommerce.SUBITO:
                prompt_answer_format = textwrap.dedent("""
                Rispondi solo con il nome della categoria e del suo gruppo di appartenenza, senza aggiungere alcuna parola.
                Le categorie sono di due livelli, voglio una risposta nel formato `Gruppo -> Categoria scelta`.
                """)
            case Ecommerce.VINTED:
                prompt_answer_format = textwrap.dedent("""
                Rispondi solo con il nome della categoria e dei sui gruppi di appartenenza, senza aggiungere alcuna parola.
                Le categorie sono di tre livelli, voglio una risposta nel formato `Gruppo -> Sottogruppo -> Categoria scelta`.
                """)

        prompt = textwrap.dedent("""
        Ti invierò in un primo blocco di testo il nome e la descrizione di un certo prodotto.
        In un secondo blocco di testo ti invierò poi un elenco di possibili categorie.
        I blocchi sono separati da caratteri dash "-------------------------".
        Indicami tra quelle possibili la categoria più adatta per il prodotto che ti ho indicato.
        Importante: NON inventare alcuna nuova categoria, scegli tra una di quelle proposte.
        {prompt_answer_format}
        --------------------------------------------------------------------------------- 
        Nome prodotto: [{product_name}]
        
        Descrizione prodotto:
        {product_description}
        ---------------------------------------------------------------------------------
        {available_categories}\
        """).format(
            prompt_answer_format=prompt_answer_format,
            product_name=product_name,
            product_description=product_description,
            available_categories=self._load_categories(ecommerce)
        )

        client = OpenAI(
            base_url="http://127.0.0.1:8000/v1",
            api_key="omlx-xxxxxxxxxxxxxxxx",
        )

        response = client.chat.completions.create(
            model="Qwen2.5-32B-Instruct-4bit",
            messages=[ChatCompletionUserMessageParam(content=prompt, role="user")],
        )

        return response.choices[0].message.content.strip()

    def _load_categories(self, ecommerce: Ecommerce) -> str:
        filename = {
            Ecommerce.SUBITO: "subito-categories.md",
            Ecommerce.VINTED: "vinted-categories.md",
        }[ecommerce]
        return (
            files("sellitai.resources")
            .joinpath(filename)
            .read_text(encoding="utf-8")
        )
