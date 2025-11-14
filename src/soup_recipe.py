from typing import List
from recipe_template import Recipe

class SoupRecipe(Recipe):
    def __init__(self):
        super().__init__("Zupa Pomidorowa", 10, 30)

    def gather_ingredients(self, steps: List[str]):
        steps.append("\n[KROK 1] Zbierz skladniki:")
        steps.append("  - Pomidory 1kg")
        steps.append("  - Bulion 1l")
        steps.append("  - Smietanka 200ml")
        steps.append("  - Cebula 1 szt")
        steps.append("  - Makaron drobny 100g")

    def prepare_ingredients(self, steps: List[str]):
        steps.append("\n[KROK 2] Przygotuj skladniki:")
        steps.append("  - Pokroj pomidory")
        steps.append("  - Posiekaj cebule")
        steps.append("  - Odmierz makaron")

    def cook(self, steps: List[str]):
        steps.append("\n[KROK 3] Gotuj:")
        steps.append("  - Podsmaż cebule")
        steps.append("  - Dodaj pomidory, duś 10 min")
        steps.append("  - Zalej bulionem")
        steps.append("  - Gotuj 15 min")
        steps.append("  - Zmiksuj")
        steps.append("  - Dodaj smietanke i makaron")
        steps.append("  - Gotuj 5 min")

    def serve(self, steps: List[str]):
        steps.append("\n[KROK 4] Podaj danie:")
        steps.append("  - Przelej do misek")
        steps.append("  - Dodaj groszek ptysiowy")