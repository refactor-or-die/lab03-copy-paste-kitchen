from recipe_template_method import Recipe

class PizzaRecipe(Recipe):
    
    def __init__(self):
        self.name = "Pizza Margherita"
        self.prep_time = 15
        self.cook_time = 25

    def gather_ingredients(self) -> str:

        steps = []

        steps.append("  - Maka 300g")
        steps.append("  - Drozdze 7g")
        steps.append("  - Sos pomidorowy 200ml")
        steps.append("  - Mozzarella 200g")
        steps.append("  - Bazylia swieża")

        return "\n".join(steps)

    def prepare_ingredients(self) -> str:

        steps = []

        steps.append("  - Zrob ciasto z maki, drozdzy i wody")
        steps.append("  - Zostaw do wyrośniecia 1h")
        steps.append("  - Pokroj mozzarelle")

        return "\n".join(steps)

    def cook(self) -> str:

        steps = []

        steps.append("  - Nagrzej piekarnik do 220°C")
        steps.append("  - Rozwałkuj ciasto")
        steps.append("  - Posmaruj sosem")
        steps.append("  - Poloz ser")
        steps.append("  - Piecz 15 min")

        return "\n".join(steps)

    def serve(self) -> str:

        steps = []

        steps.append("  - Wyjmij z piekarnika")
        steps.append("  - Dodaj swieża bazylie")
        steps.append("  - Pokroj na kawalki")
        
        return "\n".join(steps)