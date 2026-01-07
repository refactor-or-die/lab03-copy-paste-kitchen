from abc import ABC, abstractmethod
from typing import List, Dict


class Recipe(ABC):
    """Template Method – definicja algorytmu przepisu."""

    def __init__(self, name: str, prep_time: int, cook_time: int):
        self.name = name
        self.prep_time = prep_time
        self.cook_time = cook_time


    def prepare(self) -> Dict:
        steps = []


        steps += self.header()


        steps.append("\n[KROK 1] Zbierz skladniki:")
        steps += self.ingredients()


        steps.append("\n[KROK 2] Przygotuj skladniki:")
        steps += self.preparation()


        steps.append("\n[KROK 3] Gotuj:")
        steps += self.cooking()


        steps.append("\n[KROK 4] Podaj danie:")
        steps += self.serving()


        steps += self.footer()

        result = "\n".join(steps)
        print(result)

        return {
            "name": self.name,
            "prep_time": self.prep_time,
            "cook_time": self.cook_time,
            "total_time": self.prep_time + self.cook_time,
            "steps": steps
        }



    def header(self) -> List[str]:
        return [
            "=" * 50,
            f"PRZEPIS: {self.name}",
            f"Czas przygotowania: {self.prep_time} min",
            f"Czas gotowania: {self.cook_time} min",
            "=" * 50,
        ]

    def footer(self) -> List[str]:
        return [
            "\n" + "=" * 50,
            "SMACZNEGO!",
            "=" * 50,
        ]



    @abstractmethod
    def ingredients(self) -> List[str]:
        pass

    @abstractmethod
    def preparation(self) -> List[str]:
        pass

    @abstractmethod
    def cooking(self) -> List[str]:
        pass

    @abstractmethod
    def serving(self) -> List[str]:
        pass




class PastaRecipe(Recipe):
    def __init__(self):
        super().__init__("Spaghetti Bolognese", 10, 20)

    def ingredients(self):
        return [
            "  - Makaron spaghetti 250g",
            "  - Mielone mieso 300g",
            "  - Sos pomidorowy 400ml",
            "  - Cebula 1 szt",
            "  - Czosnek 2 zabki",
        ]

    def preparation(self):
        return [
            "  - Pokroj cebule w kostke",
            "  - Posiekaj czosnek",
            "  - Odmierz makaron",
        ]

    def cooking(self):
        return [
            "  - Zagotuj wode z sola",
            "  - Wrzuc makaron, gotuj 10 min",
            "  - Podsmaz cebule i czosnek",
            "  - Dodaj mieso, smaz 5 min",
            "  - Dodaj sos, gotuj 10 min",
        ]

    def serving(self):
        return [
            "  - Odcedz makaron",
            "  - Polej sosem",
            "  - Posyp parmezanem",
        ]


class PizzaRecipe(Recipe):
    def __init__(self):
        super().__init__("Pizza Margherita", 15, 25)

    def ingredients(self):
        return [
            "  - Maka 300g",
            "  - Drozdze 7g",
            "  - Sos pomidorowy 200ml",
            "  - Mozzarella 200g",
            "  - Bazylia swieza",
        ]

    def preparation(self):
        return [
            "  - Zrob ciasto z maki, drozdzy i wody",
            "  - Zostaw do wyrosniecia 1h",
            "  - Pokroj mozzarelle",
        ]

    def cooking(self):
        return [
            "  - Nagrzej piekarnik do 220C",
            "  - Rozwałkuj ciasto",
            "  - Posmaruj sosem",
            "  - Poloz ser",
            "  - Piecz 15 min",
        ]

    def serving(self):
        return [
            "  - Wyjmij z piekarnika",
            "  - Dodaj swieża bazylie",
            "  - Pokroj na kawalki",
        ]


class SaladRecipe(Recipe):
    def __init__(self):
        super().__init__("Salatka Grecka", 15, 0)

    def ingredients(self):
        return [
            "  - Pomidor 3 szt",
            "  - Ogorek 1 szt",
            "  - Feta 150g",
            "  - Oliwki 100g",
            "  - Oliwa z oliwek",
        ]

    def preparation(self):
        return [
            "  - Pokroj pomidory w osemki",
            "  - Pokroj ogorka w plastry",
            "  - Pokrusz fete",
        ]

    def cooking(self):
        return [
            "  - Wymieszaj warzywa w misce",
            "  - Dodaj oliwki",
            "  - Polej oliwa",
            "  - Posyp feta",
        ]

    def serving(self):
        return [
            "  - Przeloz na talerz",
            "  - Posyp oregano",
        ]


class SoupRecipe(Recipe):
    def __init__(self):
        super().__init__("Zupa Pomidorowa", 10, 30)

    def ingredients(self):
        return [
            "  - Pomidory 1kg",
            "  - Bulion 1l",
            "  - Smietanka 200ml",
            "  - Cebula 1 szt",
            "  - Makaron drobny 100g",
        ]

    def preparation(self):
        return [
            "  - Pokroj pomidory",
            "  - Posiekaj cebule",
            "  - Odmierz makaron",
        ]

    def cooking(self):
        return [
            "  - Podsmaz cebule",
            "  - Dodaj pomidory, dus 10 min",
            "  - Zalej bulionem",
            "  - Gotuj 15 min",
            "  - Zmiksuj",
            "  - Dodaj smietanke i makaron",
            "  - Gotuj 5 min",
        ]

    def serving(self):
        return [
            "  - Przelej do misek",
            "  - Dodaj groszek ptysiowy",
        ]



if __name__ == "__main__":
    print("\n>>> TEST SYSTEMU PRZEPISOW <<<\n")

    recipes = [
        PastaRecipe(),
        PizzaRecipe(),
        SaladRecipe(),
        SoupRecipe()
    ]

    for recipe in recipes:
        result = recipe.prepare()
        print(f"\nCzas calkowity: {result['total_time']} min")
        print("\n" + "~" * 70 + "\n")
