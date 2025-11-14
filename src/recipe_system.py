"""
System przepisow kulinarnych - ZREFAKTORYZOWANY!
Uzywamy wzorca Template Method aby wyeliminowac duplikacje.

Wzorzec Template Method definiuje szkielet algorytmu w klasie bazowej,
pozwalajac podklasom nadpisac wybrane kroki bez zmiany struktury.
"""
from abc import ABC, abstractmethod
from typing import List, Dict


class Recipe(ABC):
    """
    Abstrakcyjna klasa bazowa dla przepisow.
    Implementuje wzorzec Template Method.
    """

    def __init__(self):
        """Inicjalizacja - podklasy musza ustawic nazwe i czasy"""
        self.name = ""
        self.prep_time = 0
        self.cook_time = 0

    def prepare(self) -> Dict:
        """
        TEMPLATE METHOD - szkielet algorytmu.
        Definiuje staly przebieg przygotowania przepisu.
        Ta metoda NIE jest nadpisywana w podklasach!
        """
        steps = []

        # Krok 1: Naglowek (wspolny dla wszystkich)
        self._add_header(steps)

        # Krok 2: Skladniki (rozne dla kazdego przepisu)
        steps.append("\n[KROK 1] Zbierz skladniki:")
        self.gather_ingredients(steps)

        # Krok 3: Przygotowanie (rozne dla kazdego przepisu)
        steps.append("\n[KROK 2] Przygotuj skladniki:")
        self.prepare_ingredients(steps)

        # Krok 4: Gotowanie (rozne dla kazdego przepisu)
        steps.append("\n[KROK 3] Gotuj:")
        self.cook(steps)

        # Krok 5: Podawanie (rozne dla kazdego przepisu)
        steps.append("\n[KROK 4] Podaj danie:")
        self.serve(steps)

        # Krok 6: Stopka (wspolna dla wszystkich)
        self._add_footer(steps)

        # Wyswietl i zwroc wynik
        result = "\n".join(steps)
        print(result)

        return {
            "name": self.name,
            "prep_time": self.prep_time,
            "cook_time": self.cook_time,
            "total_time": self.prep_time + self.cook_time,
            "steps": steps
        }

    def _add_header(self, steps: List[str]) -> None:
        """Dodaje naglowek - wspolne dla wszystkich przepisow"""
        steps.append("=" * 50)
        steps.append(f"PRZEPIS: {self.name}")
        steps.append(f"Czas przygotowania: {self.prep_time} min")
        steps.append(f"Czas gotowania: {self.cook_time} min")
        steps.append("=" * 50)

    def _add_footer(self, steps: List[str]) -> None:
        """Dodaje stopke - wspolna dla wszystkich przepisow"""
        steps.append("\n" + "=" * 50)
        steps.append("SMACZNEGO!")
        steps.append("=" * 50)

    # Metody abstrakcyjne - MUSZA byc zaimplementowane w podklasach

    @abstractmethod
    def gather_ingredients(self, steps: List[str]) -> None:
        """Zbierz skladniki specyficzne dla danego przepisu"""
        pass

    @abstractmethod
    def prepare_ingredients(self, steps: List[str]) -> None:
        """Przygotuj skladniki specyficzne dla danego przepisu"""
        pass

    @abstractmethod
    def cook(self, steps: List[str]) -> None:
        """Gotuj wedlug specyfiki danego przepisu"""
        pass

    @abstractmethod
    def serve(self, steps: List[str]) -> None:
        """Podaj danie wedlug specyfiki przepisu"""
        pass


class PastaRecipe(Recipe):
    """Przepis na makaron - tylko specyficzne szczegoly!"""

    def __init__(self):
        super().__init__()
        self.name = "Spaghetti Bolognese"
        self.prep_time = 10
        self.cook_time = 20

    def gather_ingredients(self, steps: List[str]) -> None:
        steps.append("  - Makaron spaghetti 250g")
        steps.append("  - Mielone mieso 300g")
        steps.append("  - Sos pomidorowy 400ml")
        steps.append("  - Cebula 1 szt")
        steps.append("  - Czosnek 2 zabki")

    def prepare_ingredients(self, steps: List[str]) -> None:
        steps.append("  - Pokroj cebule w kostke")
        steps.append("  - Posiekaj czosnek")
        steps.append("  - Odmierz makaron")

    def cook(self, steps: List[str]) -> None:
        steps.append("  - Zagotuj wode z sola")
        steps.append("  - Wrzuc makaron, gotuj 10 min")
        steps.append("  - Podsmaż cebule i czosnek")
        steps.append("  - Dodaj mieso, smaż 5 min")
        steps.append("  - Dodaj sos, gotuj 10 min")

    def serve(self, steps: List[str]) -> None:
        steps.append("  - Odcedz makaron")
        steps.append("  - Polej sosem")
        steps.append("  - Posyp parmezanem")


class PizzaRecipe(Recipe):
    """Przepis na pizze - tylko specyficzne szczegoly!"""

    def __init__(self):
        super().__init__()
        self.name = "Pizza Margherita"
        self.prep_time = 15
        self.cook_time = 25

    def gather_ingredients(self, steps: List[str]) -> None:
        steps.append("  - Maka 300g")
        steps.append("  - Drozdze 7g")
        steps.append("  - Sos pomidorowy 200ml")
        steps.append("  - Mozzarella 200g")
        steps.append("  - Bazylia swieża")

    def prepare_ingredients(self, steps: List[str]) -> None:
        steps.append("  - Zrob ciasto z maki, drozdzy i wody")
        steps.append("  - Zostaw do wyrośniecia 1h")
        steps.append("  - Pokroj mozzarelle")

    def cook(self, steps: List[str]) -> None:
        steps.append("  - Nagrzej piekarnik do 220°C")
        steps.append("  - Rozwałkuj ciasto")
        steps.append("  - Posmaruj sosem")
        steps.append("  - Poloz ser")
        steps.append("  - Piecz 15 min")

    def serve(self, steps: List[str]) -> None:
        steps.append("  - Wyjmij z piekarnika")
        steps.append("  - Dodaj swieża bazylie")
        steps.append("  - Pokroj na kawalki")


class SaladRecipe(Recipe):
    """Przepis na salatke - tylko specyficzne szczegoly!"""

    def __init__(self):
        super().__init__()
        self.name = "Salatka Grecka"
        self.prep_time = 15
        self.cook_time = 0  # Salatka nie wymaga gotowania!

    def gather_ingredients(self, steps: List[str]) -> None:
        steps.append("  - Pomidor 3 szt")
        steps.append("  - Ogorek 1 szt")
        steps.append("  - Feta 150g")
        steps.append("  - Oliwki 100g")
        steps.append("  - Oliwa z oliwek")

    def prepare_ingredients(self, steps: List[str]) -> None:
        steps.append("  - Pokroj pomidory w osemki")
        steps.append("  - Pokroj ogorka w plastry")
        steps.append("  - Pokrusz fete")

    def cook(self, steps: List[str]) -> None:
        steps.append("  - Wymieszaj warzywa w misce")
        steps.append("  - Dodaj oliwki")
        steps.append("  - Polej oliwa")
        steps.append("  - Posyp feta")

    def serve(self, steps: List[str]) -> None:
        steps.append("  - Przeloz na talerz")
        steps.append("  - Posyp oregano")


class SoupRecipe(Recipe):
    """Przepis na zupe - tylko specyficzne szczegoly!"""

    def __init__(self):
        super().__init__()
        self.name = "Zupa Pomidorowa"
        self.prep_time = 10
        self.cook_time = 30

    def gather_ingredients(self, steps: List[str]) -> None:
        steps.append("  - Pomidory 1kg")
        steps.append("  - Bulion 1l")
        steps.append("  - Smietanka 200ml")
        steps.append("  - Cebula 1 szt")
        steps.append("  - Makaron drobny 100g")

    def prepare_ingredients(self, steps: List[str]) -> None:
        steps.append("  - Pokroj pomidory")
        steps.append("  - Posiekaj cebule")
        steps.append("  - Odmierz makaron")

    def cook(self, steps: List[str]) -> None:
        steps.append("  - Podsmaż cebule")
        steps.append("  - Dodaj pomidory, duś 10 min")
        steps.append("  - Zalej bulionem")
        steps.append("  - Gotuj 15 min")
        steps.append("  - Zmiksuj")
        steps.append("  - Dodaj smietanke i makaron")
        steps.append("  - Gotuj 5 min")

    def serve(self, steps: List[str]) -> None:
        steps.append("  - Przelej do misek")
        steps.append("  - Dodaj groszek ptysiowy")


# Przykladowe uzycie
if __name__ == "__main__":
    print("\n>>> TESTOWANIE SYSTEMU PRZEPISOW <<<\n")

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