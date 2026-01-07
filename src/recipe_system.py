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
    def prepare(self) -> Dict:
        self.init_steps()
        self.header()
        self.gatherIngredients()
        self.prepwork()
        self.cook()
        self.serve()
        self.footer()
        result = "\n".join(self.steps)
        print(result)
        return {
            "name": self.name,
            "prep_time": self.prep_time,
            "cook_time": self.cook_time,
            "total_time": self.prep_time + self.cook_time,
            "steps": self.steps
        }

    def init_steps(self):
        self.steps = []
    
    def header(self):
        self.steps.append("=" * 50)
        self.steps.append(f"PRZEPIS: {self.name}")
        self.steps.append(f"Czas przygotowania: {self.prep_time} min")
        self.steps.append(f"Czas gotowania: {self.cook_time} min")
        self.steps.append("=" * 50)
    
    @abstractmethod
    def gatherIngredients(self):
        pass
    @abstractmethod
    def prepwork(self):
        pass
    @abstractmethod
    def cook(self):
        pass
    @abstractmethod
    def serve(self):
        pass
        
    def footer(self):
        self.steps.append("\n" + "=" * 50)
        self.steps.append("SMACZNEGO!")
        self.steps.append("=" * 50)

class PastaRecipe(Recipe):
    """Przepis na makaron - pelno powielonego kodu!"""
    
    def __init__(self):
        self.name = "Spaghetti Bolognese"
        self.prep_time = 10
        self.cook_time = 20
        
    def gatherIngredients(self):
        self.steps.append("\n[KROK 1] Zbierz skladniki:")
        self.steps.append("  - Makaron spaghetti 250g")
        self.steps.append("  - Mielone mieso 300g")
        self.steps.append("  - Sos pomidorowy 400ml")
        self.steps.append("  - Cebula 1 szt")
        self.steps.append("  - Czosnek 2 zabki")
        
    def prepwork(self):
        self.steps.append("\n[KROK 2] Przygotuj skladniki:")
        self.steps.append("  - Pokroj cebule w kostke")
        self.steps.append("  - Posiekaj czosnek")
        self.steps.append("  - Odmierz makaron")
        
    def cook(self):
        self.steps.append("\n[KROK 3] Gotuj:")
        self.steps.append("  - Zagotuj wode z sola")
        self.steps.append("  - Wrzuc makaron, gotuj 10 min")
        self.steps.append("  - Podsmaż cebule i czosnek")
        self.steps.append("  - Dodaj mieso, smaż 5 min")
        self.steps.append("  - Dodaj sos, gotuj 10 min")
        
    def serve(self):
        self.steps.append("\n[KROK 4] Podaj danie:")
        self.steps.append("  - Odcedz makaron")
        self.steps.append("  - Polej sosem")
        self.steps.append("  - Posyp parmezanem")
class PizzaRecipe(Recipe):
    """Przepis na pizze - ZNOWU to samo! Copy-paste!"""
    
    def __init__(self):
        self.name = "Pizza Margherita"
        self.prep_time = 15
        self.cook_time = 25
        
    def gatherIngredients(self):
        self.steps.append("\n[KROK 1] Zbierz skladniki:")
        self.steps.append("  - Maka 300g")
        self.steps.append("  - Drozdze 7g")
        self.steps.append("  - Sos pomidorowy 200ml")
        self.steps.append("  - Mozzarella 200g")
        self.steps.append("  - Bazylia swieża")
        
    def prepwork(self):
        self.steps.append("\n[KROK 2] Przygotuj skladniki:")
        self.steps.append("  - Zrob ciasto z maki, drozdzy i wody")
        self.steps.append("  - Zostaw do wyrośniecia 1h")
        self.steps.append("  - Pokroj mozzarelle")
        
    def cook(self):
        self.steps.append("\n[KROK 3] Gotuj:")
        self.steps.append("  - Nagrzej piekarnik do 220°C")
        self.steps.append("  - Rozwałkuj ciasto")
        self.steps.append("  - Posmaruj sosem")
        self.steps.append("  - Poloz ser")
        self.steps.append("  - Piecz 15 min")
        
    def serve(self):
        self.steps.append("\n[KROK 4] Podaj danie:")
        self.steps.append("  - Wyjmij z piekarnika")
        self.steps.append("  - Dodaj swieża bazylie")
        self.steps.append("  - Pokroj na kawalki")


class SaladRecipe(Recipe):
    """Przepis na salatke - JESZCZE WIECEJ kopii tego samego!"""
    
    def __init__(self):
        self.name = "Salatka Grecka"
        self.prep_time = 15
        self.cook_time = 0  # Salatka nie wymaga gotowania!
        
    def gatherIngredients(self):
        self.steps.append("\n[KROK 1] Zbierz skladniki:")
        self.steps.append("  - Pomidor 3 szt")
        self.steps.append("  - Ogorek 1 szt")
        self.steps.append("  - Feta 150g")
        self.steps.append("  - Oliwki 100g")
        self.steps.append("  - Oliwa z oliwek")
        
    def prepwork(self):
        self.steps.append("\n[KROK 2] Przygotuj skladniki:")
        self.steps.append("  - Pokroj pomidory w osemki")
        self.steps.append("  - Pokroj ogorka w plastry")
        self.steps.append("  - Pokrusz fete")
        
    def cook(self):
        self.steps.append("\n[KROK 3] Gotuj:")
        self.steps.append("  - Wymieszaj warzywa w misce")
        self.steps.append("  - Dodaj oliwki")
        self.steps.append("  - Polej oliwa")
        self.steps.append("  - Posyp feta")
        
    def serve(self):
        self.steps.append("\n[KROK 4] Podaj danie:")
        self.steps.append("  - Przeloz na talerz")
        self.steps.append("  - Posyp oregano")


class SoupRecipe(Recipe):
    """Przepis na zupe - i tu tez kopiujemy jak szaleni!"""
    
    def __init__(self):
        self.name = "Zupa Pomidorowa"
        self.prep_time = 10
        self.cook_time = 30
        
    def gatherIngredients(self):
        self.steps.append("\n[KROK 1] Zbierz skladniki:")
        self.steps.append("  - Pomidory 1kg")
        self.steps.append("  - Bulion 1l")
        self.steps.append("  - Smietanka 200ml")
        self.steps.append("  - Cebula 1 szt")
        self.steps.append("  - Makaron drobny 100g")
        
    def prepwork(self):
        self.steps.append("\n[KROK 2] Przygotuj skladniki:")
        self.steps.append("  - Pokroj pomidory")
        self.steps.append("  - Posiekaj cebule")
        self.steps.append("  - Odmierz makaron")
        
    def cook(self):
        self.steps.append("\n[KROK 3] Gotuj:")
        self.steps.append("  - Podsmaż cebule")
        self.steps.append("  - Dodaj pomidory, duś 10 min")
        self.steps.append("  - Zalej bulionem")
        self.steps.append("  - Gotuj 15 min")
        self.steps.append("  - Zmiksuj")
        self.steps.append("  - Dodaj smietanke i makaron")
        self.steps.append("  - Gotuj 5 min")
        
    def serve(self):
        self.steps.append("\n[KROK 4] Podaj danie:")
        self.steps.append("  - Przelej do misek")
        self.steps.append("  - Dodaj groszek ptysiowy")
        
       


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
