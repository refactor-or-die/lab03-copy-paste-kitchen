from recipe_template_method import Recipe

class SoupRecipe(Recipe):
    
    def __init__(self):
        self.name = "Zupa Pomidorowa"
        self.prep_time = 10
        self.cook_time = 30

    def get_name(self) -> str:
        return self.name

    def get_prep_time(self) -> int:
        return self.prep_time

    def get_cook_time(self) -> int:
        return self.cook_time

    def gather_ingredients(self) -> str:

        steps = []

        steps.append("\n[KROK 1] Zbierz skladniki:")
        steps.append("  - Pomidory 1kg")
        steps.append("  - Bulion 1l")
        steps.append("  - Smietanka 200ml")
        steps.append("  - Cebula 1 szt")
        steps.append("  - Makaron drobny 100g")

        return "\n".join(steps)

    def prepare_ingredients(self) -> str:

        steps = []

        steps.append("\n[KROK 2] Przygotuj skladniki:")
        steps.append("  - Pokroj pomidory")
        steps.append("  - Posiekaj cebule")
        steps.append("  - Odmierz makaron")

        return "\n".join(steps)

    def cook(self) -> str:

        steps = []

        steps.append("\n[KROK 3] Gotuj:")
        steps.append("  - Podsmaż cebule")
        steps.append("  - Dodaj pomidory, duś 10 min")
        steps.append("  - Zalej bulionem")
        steps.append("  - Gotuj 15 min")
        steps.append("  - Zmiksuj")
        steps.append("  - Dodaj smietanke i makaron")
        steps.append("  - Gotuj 5 min")

        return "\n".join(steps)

    def serve(self) -> str:

        steps = []

        steps.append("\n[KROK 4] Podaj danie:")
        steps.append("  - Przelej do misek")
        steps.append("  - Dodaj groszek ptysiowy")
        
        return "\n".join(steps)