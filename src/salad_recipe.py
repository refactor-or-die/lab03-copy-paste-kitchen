from recipe_template_method import Recipe

class SaladRecipe(Recipe):
    
    def __init__(self):
        self.name = "Salatka Grecka"
        self.prep_time = 15
        self.cook_time = 0  # Salatka nie wymaga gotowania!

    def gather_ingredients(self) -> str:

        steps = []

        steps.append("  - Pomidor 3 szt")
        steps.append("  - Ogorek 1 szt")
        steps.append("  - Feta 150g")
        steps.append("  - Oliwki 100g")
        steps.append("  - Oliwa z oliwek")

        return "\n".join(steps)

    def prepare_ingredients(self) -> str:

        steps = []

        steps.append("  - Pokroj pomidory w osemki")
        steps.append("  - Pokroj ogorka w plastry")
        steps.append("  - Pokrusz fete")

        return "\n".join(steps)

    def cook(self) -> str:

        steps = []

        steps.append("  - Wymieszaj warzywa w misce")
        steps.append("  - Dodaj oliwki")
        steps.append("  - Polej oliwa")
        steps.append("  - Posyp feta")

        return "\n".join(steps)

    def serve(self) -> str:

        steps = []

        steps.append("  - Przeloz na talerz")
        steps.append("  - Posyp oregano")
        
        return "\n".join(steps)