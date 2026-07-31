import textwrap

from openai import OpenAI
from openai.types.chat import ChatCompletionUserMessageParam

from sellitai.categorizer.interfaces import ProductCategorizer


class OpenAIApiProductCategorizer(ProductCategorizer):

    def category_for(
        self,
        product_name: str,
        product_description: str,
        available_categories: str,
    ) -> str:
        prompt = textwrap.dedent("""
        Ti invierò in un primo blocco di testo il nome e la descrizione di un certo prodotto.
        In un secondo blocco di testo ti invierò poi un elenco di possibili categorie. Sono 38 categorie totali suddivise in 7 gruppi.
        I blocchi sono separati da caratteri dash "-------------------------".
        Vorrei mi indicassi la categoria più adatta per il prodotto che ti ho indicato e il gruppo a cui questa appartiene.
        Rispondi solo con il nome della categoria (e del suo gruppo di appartenenza) nel formato "Gruppo -> Categoria" senza aggiungere alcuna parola.
        Esempio di risposta: "Elettronica -> Informatica"
        --------------------------------------------------------------------------------- 
        Nome prodotto: [{product_name}]
        
        Descrizione prodotto:
        {product_description}
        ---------------------------------------------------------------------------------
        {available_categories}\
        """).format(
            product_name=product_name,
            product_description=product_description,
            available_categories=available_categories
        )

        client = OpenAI(
            base_url="http://127.0.0.1:8000/v1",
            api_key="omlx-xxxxxxxxxxxxxxxx",
        )

        response = client.chat.completions.create(
            model="Qwen3-Coder-30B-A3B-Instruct-MLX-4bit",
            messages=[ChatCompletionUserMessageParam(content=prompt, role="user")],
        )

        return response.choices[0].message.content.strip()
