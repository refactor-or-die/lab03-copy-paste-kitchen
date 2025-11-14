from recipe_template_method import Recipe

class PizzaRecipe(Recipe):
    
    def __init__(self):
        self.name = "Pizza Margherita"
        self.prep_time = 15
        self.cook_time = 25

    def get_name(self) -> str:
        return self.name

    def get_prep_time(self) -> int:
        return self.prep_time

    def get_cook_time(self) -> int:
        return self.cook_time

    def gather_ingredients(self) -> str:

        steps = []
        
        steps.append("\n[KROK 1] Zbierz skladniki:")
        steps.append("  - Maka 300g")
        steps.append("  - Drozdze 7g")
        steps.append("  - Sos pomidorowy 200ml")
        steps.append("  - Mozzarella 200g")
        steps.append("  - Bazylia swieża")

        return "\n".join(steps)

    def prepare_ingredients(self) -> str:

        steps = []

        steps.append("\n[KROK 2] Przygotuj skladniki:")
        steps.append("  - Zrob ciasto z maki, drozdzy i wody")
        steps.append("  - Zostaw do wyrośniecia 1h")
        steps.append("  - Pokroj mozzarelle")

        return "\n".join(steps)

    def cook(self) -> str:

        steps = []

        steps.append("\n[KROK 3] Gotuj:")
        steps.append("  - Nagrzej piekarnik do 220°C")
        steps.append("  - Rozwałkuj ciasto")
        steps.append("  - Posmaruj sosem")
        steps.append("  - Poloz ser")
        steps.append("  - Piecz 15 min")

        return "\n".join(steps)

    def serve(self) -> str:

        steps = []

        steps.append("\n[KROK 4] Podaj danie:")
        steps.append("  - Wyjmij z piekarnika")
        steps.append("  - Dodaj swieża bazylie")
        steps.append("  - Pokroj na kawalki")
        
        return "\n".join(steps)