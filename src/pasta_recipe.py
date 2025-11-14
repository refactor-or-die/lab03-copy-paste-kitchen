from recipe_template_method import Recipe

class PastaRecipe(Recipe):
    
    def __init__(self):
        self.name = "Spaghetti Bolognese"
        self.prep_time = 10
        self.cook_time = 20

    def gather_ingredients(self) -> str:

        steps = []
        
        steps.append("\n[KROK 1] Zbierz skladniki:")
        steps.append("  - Makaron spaghetti 250g")
        steps.append("  - Mielone mieso 300g")
        steps.append("  - Sos pomidorowy 400ml")
        steps.append("  - Cebula 1 szt")
        steps.append("  - Czosnek 2 zabki")

        return "\n".join(steps)

    def prepare_ingredients(self) -> str:

        steps = []

        steps.append("\n[KROK 2] Przygotuj skladniki:")
        steps.append("  - Pokroj cebule w kostke")
        steps.append("  - Posiekaj czosnek")
        steps.append("  - Odmierz makaron")

        return "\n".join(steps)

    def cook(self) -> str:

        steps = []

        steps.append("\n[KROK 3] Gotuj:")
        steps.append("  - Zagotuj wode z sola")
        steps.append("  - Wrzuc makaron, gotuj 10 min")
        steps.append("  - Podsmaż cebule i czosnek")
        steps.append("  - Dodaj mieso, smaż 5 min")
        steps.append("  - Dodaj sos, gotuj 10 min")

        return "\n".join(steps)

    def serve(self) -> str:

        steps = []

        steps.append("\n[KROK 4] Podaj danie:")
        steps.append("  - Odcedz makaron")
        steps.append("  - Polej sosem")
        steps.append("  - Posyp parmezanem")
        
        return "\n".join(steps)