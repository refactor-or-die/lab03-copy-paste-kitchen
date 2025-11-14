"""
System przepisow kulinarnych.
UWAGA: Ten kod ma MNÓSTWO duplikacji! Uzyj wzorca Template Method.

Kazdy przepis ma te same kroki:
1. Wyswietl naglowek
2. Zbierz skladniki
3. Przygotuj
4. Gotuj
5. Podaj
6. Wyswietl stopke

Ale szczegoly sa rozne dla kazdego przepisu!
"""

from abc import ABC, abstractmethod


class Recipe(ABC):
    def __init__(self, /, name: str, prep_time: int, cook_time: int):
        self.name = name
        self.prep_time = prep_time
        self.cook_time = cook_time

    def prepare(self) -> dict:
        """Przygotuj danie wedlug przepisu"""
        steps = []

        # Naglowek
        steps.append("=" * 50)
        steps.append(f"PRZEPIS: {self.name}")
        steps.append(f"Czas przygotowania: {self.prep_time} min")
        steps.append(f"Czas gotowania: {self.cook_time} min")
        steps.append("=" * 50)

        steps.append("\n[KROK 1] Zbierz skladniki:")
        steps.extend(self.ingredients())

        steps.append("\n[KROK 2] Przygotuj skladniki:")
        steps.extend(self.preparation())

        steps.append("\n[KROK 3] Gotuj:")
        steps.extend(self.cooking())

        steps.append("\n[KROK 4] Podaj danie:")
        steps.extend(self.serving())

        # Stopka
        steps.append("\n" + "=" * 50)
        steps.append("SMACZNEGO!")
        steps.append("=" * 50)

        result = "\n".join(steps)
        print(result)

        return {
            "name": self.name,
            "prep_time": self.prep_time,
            "cook_time": self.cook_time,
            "total_time": self.prep_time + self.cook_time,
            "steps": steps,
        }

    @abstractmethod
    def ingredients(self) -> list[str]:
        pass

    @abstractmethod
    def preparation(self) -> list[str]:
        pass

    @abstractmethod
    def cooking(self) -> list[str]:
        pass

    @abstractmethod
    def serving(self) -> list[str]:
        pass


class PastaRecipe(Recipe):
    """Przepis na makaron - pelno powielonego kodu!"""

    def __init__(self):
        super().__init__(
            name="Spaghetti Bolognese",
            prep_time=10,
            cook_time=20,
        )

    def ingredients(self) -> list[str]:
        steps = []
        steps.append("  - Makaron spaghetti 250g")
        steps.append("  - Mielone mieso 300g")
        steps.append("  - Sos pomidorowy 400ml")
        steps.append("  - Cebula 1 szt")
        steps.append("  - Czosnek 2 zabki")
        return steps

    def preparation(self) -> list[str]:
        steps = []
        steps.append("  - Pokroj cebule w kostke")
        steps.append("  - Posiekaj czosnek")
        steps.append("  - Odmierz makaron")
        return steps

    def cooking(self) -> list[str]:
        steps = []
        steps.append("  - Zagotuj wode z sola")
        steps.append("  - Wrzuc makaron, gotuj 10 min")
        steps.append("  - Podsmaż cebule i czosnek")
        steps.append("  - Dodaj mieso, smaż 5 min")
        steps.append("  - Dodaj sos, gotuj 10 min")
        return steps

    def serving(self) -> list[str]:
        steps = []
        steps.append("  - Odcedz makaron")
        steps.append("  - Polej sosem")
        steps.append("  - Posyp parmezanem")
        return steps


class PizzaRecipe(Recipe):
    """Przepis na pizze - ZNOWU to samo! Copy-paste!"""

    def __init__(self):
        super().__init__(
            name="Pizza Margherita",
            prep_time=15,
            cook_time=25,
        )

    def ingredients(self) -> list[str]:
        steps = []
        steps.append("  - Maka 300g")
        steps.append("  - Drozdze 7g")
        steps.append("  - Sos pomidorowy 200ml")
        steps.append("  - Mozzarella 200g")
        steps.append("  - Bazylia swieża")
        return steps

    def preparation(self) -> list[str]:
        steps = []
        steps.append("  - Zrob ciasto z maki, drozdzy i wody")
        steps.append("  - Zostaw do wyrośniecia 1h")
        steps.append("  - Pokroj mozzarelle")
        return steps

    def cooking(self) -> list[str]:
        steps = []
        steps.append("  - Nagrzej piekarnik do 220°C")
        steps.append("  - Rozwałkuj ciasto")
        steps.append("  - Posmaruj sosem")
        steps.append("  - Poloz ser")
        steps.append("  - Piecz 15 min")
        return steps

    def serving(self) -> list[str]:
        steps = []
        steps.append("  - Wyjmij z piekarnika")
        steps.append("  - Dodaj swieża bazylie")
        steps.append("  - Pokroj na kawalki")
        return steps


class SaladRecipe(Recipe):
    """Przepis na salatke - JESZCZE WIECEJ kopii tego samego!"""

    def __init__(self):
        super().__init__(
            name="Salatka Grecka",
            prep_time=15,
            cook_time=0,  # Salatka nie wymaga gotowania!
        )

    def ingredients(self) -> list[str]:
        steps = []
        steps.append("  - Pomidor 3 szt")
        steps.append("  - Ogorek 1 szt")
        steps.append("  - Feta 150g")
        steps.append("  - Oliwki 100g")
        steps.append("  - Oliwa z oliwek")
        return steps

    def preparation(self) -> list[str]:
        steps = []
        steps.append("  - Pokroj pomidory w osemki")
        steps.append("  - Pokroj ogorka w plastry")
        steps.append("  - Pokrusz fete")
        return steps

    def cooking(self) -> list[str]:
        steps = []
        steps.append("  - Wymieszaj warzywa w misce")
        steps.append("  - Dodaj oliwki")
        steps.append("  - Polej oliwa")
        steps.append("  - Posyp feta")

        return steps

    def serving(self) -> list[str]:
        steps = []
        steps.append("\n[KROK 4] Podaj danie:")
        steps.append("  - Przeloz na talerz")
        steps.append("  - Posyp oregano")

        return steps


class SoupRecipe(Recipe):
    """Przepis na zupe - i tu tez kopiujemy jak szaleni!"""

    def __init__(self):
        super().__init__(
            name="Zupa Pomidorowa",
            prep_time=10,
            cook_time=30,
        )

    def ingredients(self) -> list[str]:
        steps = []
        steps.append("  - Pomidory 1kg")
        steps.append("  - Bulion 1l")
        steps.append("  - Smietanka 200ml")
        steps.append("  - Cebula 1 szt")
        steps.append("  - Makaron drobny 100g")

        return steps

    def preparation(self) -> list[str]:
        steps = []
        steps.append("  - Pokroj pomidory")
        steps.append("  - Posiekaj cebule")
        steps.append("  - Odmierz makaron")

        return steps

    def cooking(self) -> list[str]:
        steps = []
        steps.append("  - Podsmaż cebule")
        steps.append("  - Dodaj pomidory, duś 10 min")
        steps.append("  - Zalej bulionem")
        steps.append("  - Gotuj 15 min")
        steps.append("  - Zmiksuj")
        steps.append("  - Dodaj smietanke i makaron")
        steps.append("  - Gotuj 5 min")
        return steps

    def serving(self) -> list[str]:
        steps = []
        steps.append("  - Przelej do misek")
        steps.append("  - Dodaj groszek ptysiowy")
        return steps


# Przykladowe uzycie
if __name__ == "__main__":
    print("\n>>> TESTOWANIE SYSTEMU PRZEPISOW <<<\n")

    recipes = [PastaRecipe(), PizzaRecipe(), SaladRecipe(), SoupRecipe()]

    for recipe in recipes:
        result = recipe.prepare()
        print(f"\nCzas calkowity: {result['total_time']} min")
        print("\n" + "~" * 70 + "\n")
