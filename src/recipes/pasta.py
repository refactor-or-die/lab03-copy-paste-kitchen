from typing import List
from .recipe_template import Recipe


class PastaRecipe(Recipe):
    def __init__(self):
        super().__init__("Spaghetti Bolognese", 10, 20)

    def gather_ingredients(self, steps: List[str]):
        steps.append("  - Makaron spaghetti 250g")
        steps.append("  - Mielone mieso 300g")
        steps.append("  - Sos pomidorowy 400ml")
        steps.append("  - Cebula 1 szt")
        steps.append("  - Czosnek 2 zabki")

    def prepare_ingredients(self, steps: List[str]):
        steps.append("  - Pokroj cebule w kostke")
        steps.append("  - Posiekaj czosnek")
        steps.append("  - Odmierz makaron")

    def cook(self, steps: List[str]):
        steps.append("  - Zagotuj wode z sola")
        steps.append("  - Wrzuc makaron, gotuj 10 min")
        steps.append("  - Podsmaż cebule i czosnek")
        steps.append("  - Dodaj mieso, smaż 5 min")
        steps.append("  - Dodaj sos, gotuj 10 min")

    def serve(self, steps: List[str]):
        steps.append("  - Odcedz makaron")
        steps.append("  - Polej sosem")
        steps.append("  - Posyp parmezanem")
