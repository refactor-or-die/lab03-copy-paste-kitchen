

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
from typing import List, Dict
from abc import ABC, abstractmethod


class Recipe(ABC):
    def __init__(self, name, prep_time, cook_time):
        self.name = name
        self.prep_time = prep_time
        self.cook_time = cook_time
        
    def _seperator(self, steps: List[str], newline = False):
        if (newline):
            steps.append("\n" + "=" * 50)
        else:
            steps.append("=" * 50)
        

    def _footer(self, steps: List[str]):
        self._seperator(steps, newline=True)
        steps.append("SMACZNEGO!")
        self._seperator(steps)

    def _step_header(self, number, title, steps: List[str]):
        steps.append(f"\n[KROK {number}] {title}:")


    def _header(self, steps: List[str]):
        
        self._seperator(steps)
        steps.append(f"PRZEPIS: {self.name}")
        steps.append(f"Czas przygotowania: {self.prep_time} min")
        steps.append(f"Czas gotowania: {self.cook_time} min")
        self._seperator(steps)

    def prepare(self) -> Dict:
        steps = []
        self._header(steps)
        self._step_header(1, "Zbierz skladniki", steps)
        self.gather_ingredients(steps)
        self._step_header(2,"Przygotuj skladniki", steps)
        self.prepare_ingredients(steps)
        self._step_header(3,"Gotuj", steps)
        self.cook(steps)
        self._step_header(4,"Podaj danie", steps)
        self.serve(steps)
        self._footer(steps)
        result = "\n".join(steps)
        print(result)
        
        return {
            "name": self.name,
            "prep_time": self.prep_time,
            "cook_time": self.cook_time,
            "total_time": self.prep_time + self.cook_time,
            "steps": steps
        }


    
    @abstractmethod
    def gather_ingredients(self, steps: List[str]):
        pass
    
    @abstractmethod
    def prepare_ingredients(self, steps: List[str]):
        pass
        
    @abstractmethod
    def cook(self, steps: List[str]):
        pass

    @abstractmethod
    def serve(self, steps: List[str]):
        pass


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

class PizzaRecipe(Recipe):
    def __init__(self):
        super().__init__("Pizza Margherita", 15, 25)

    def gather_ingredients(self, steps: List[str]):
        steps.append("  - Maka 300g")
        steps.append("  - Drozdze 7g")
        steps.append("  - Sos pomidorowy 200ml")
        steps.append("  - Mozzarella 200g")
        steps.append("  - Bazylia swieża")
    
    def prepare_ingredients(self, steps: List[str]):
        steps.append("  - Zrob ciasto z maki, drozdzy i wody")
        steps.append("  - Zostaw do wyrośniecia 1h")
        steps.append("  - Pokroj mozzarelle")
        
    def cook(self, steps: List[str]):
        steps.append("  - Nagrzej piekarnik do 220°C")
        steps.append("  - Rozwałkuj ciasto")
        steps.append("  - Posmaruj sosem")
        steps.append("  - Poloz ser")
        steps.append("  - Piecz 15 min")

    def serve(self, steps: List[str]):
        steps.append("  - Wyjmij z piekarnika")
        steps.append("  - Dodaj swieża bazylie")
        steps.append("  - Pokroj na kawalki")
    
class SaladRecipe(Recipe):
    def __init__(self):
        super().__init__("Salatka Grecka", 15, 0)
    
    def gather_ingredients(self, steps: List[str]):
        steps.append("  - Pomidor 3 szt")
        steps.append("  - Ogorek 1 szt")
        steps.append("  - Feta 150g")
        steps.append("  - Oliwki 100g")
        steps.append("  - Oliwa z oliwek")
        
    def prepare_ingredients(self, steps: List[str]):
        steps.append("  - Pokroj pomidory w osemki")
        steps.append("  - Pokroj ogorka w plastry")
        steps.append("  - Pokrusz fete")
        
        
    def cook(self, steps: List[str]):
        steps.append("  - Wymieszaj warzywa w misce")
        steps.append("  - Dodaj oliwki")
        steps.append("  - Polej oliwa")
        steps.append("  - Posyp feta")

    def serve(self, steps: List[str]):
        steps.append("  - Przeloz na talerz")
        steps.append("  - Posyp oregano")

class SoupRecipe(Recipe):
    def __init__(self):
        super().__init__("Zupa Pomidorowa", 10, 30)
    
    def gather_ingredients(self, steps: List[str]):
        steps.append("  - Pomidory 1kg")
        steps.append("  - Bulion 1l")
        steps.append("  - Smietanka 200ml")
        steps.append("  - Cebula 1 szt")
        steps.append("  - Makaron drobny 100g")
        
    def prepare_ingredients(self, steps: List[str]):
        steps.append("  - Pokroj pomidory")
        steps.append("  - Posiekaj cebule")
        steps.append("  - Odmierz makaron")
        
    def cook(self, steps: List[str]):
        steps.append("  - Podsmaż cebule")
        steps.append("  - Dodaj pomidory, duś 10 min")
        steps.append("  - Zalej bulionem")
        steps.append("  - Gotuj 15 min")
        steps.append("  - Zmiksuj")
        steps.append("  - Dodaj smietanke i makaron")
        steps.append("  - Gotuj 5 min")

    def serve(self, steps: List[str]):
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

