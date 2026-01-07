"""
Testy jednostkowe dla systemu przepisow kulinarnych.
NIE MODYFIKUJ TESTOW! Powinny przechodzic zarowno przed jak i po refaktoryzacji.
"""
import pytest
from src.recipe_system import PastaRecipe, PizzaRecipe, SaladRecipe, SoupRecipe


class TestRecipeSystem:
    
    @pytest.fixture
    def pasta(self):
        return PastaRecipe()
    
    @pytest.fixture
    def pizza(self):
        return PizzaRecipe()
    
    @pytest.fixture
    def salad(self):
        return SaladRecipe()
    
    @pytest.fixture
    def soup(self):
        return SoupRecipe()
    
    def test_pasta_basic_info(self, pasta):
        """Test podstawowych informacji o przepisie na makaron"""
        result = pasta.prepare()
        assert result["name"] == "Spaghetti Bolognese"
        assert result["prep_time"] == 10
        assert result["cook_time"] == 20
        assert result["total_time"] == 30
    
    def test_pizza_basic_info(self, pizza):
        """Test podstawowych informacji o pizzy"""
        result = pizza.prepare()
        assert result["name"] == "Pizza Margherita"
        assert result["prep_time"] == 15
        assert result["cook_time"] == 25
        assert result["total_time"] == 40
    
    def test_salad_basic_info(self, salad):
        """Test podstawowych informacji o salatce"""
        result = salad.prepare()
        assert result["name"] == "Salatka Grecka"
        assert result["prep_time"] == 15
        assert result["cook_time"] == 0  # Salatka nie wymaga gotowania!
        assert result["total_time"] == 15
    
    def test_soup_basic_info(self, soup):
        """Test podstawowych informacji o zupie"""
        result = soup.prepare()
        assert result["name"] == "Zupa Pomidorowa"
        assert result["prep_time"] == 10
        assert result["cook_time"] == 30
        assert result["total_time"] == 40
    
    def test_pasta_has_all_steps(self, pasta):
        """Test czy przepis na makaron ma wszystkie kroki"""
        result = pasta.prepare()
        steps_text = "\n".join(result["steps"])
        
        # Sprawdz naglowek
        assert "PRZEPIS: Spaghetti Bolognese" in steps_text
        assert "Czas przygotowania: 10 min" in steps_text
        assert "Czas gotowania: 20 min" in steps_text
        
        # Sprawdz kroki
        assert "[KROK 1] Zbierz skladniki:" in steps_text
        assert "[KROK 2] Przygotuj skladniki:" in steps_text
        assert "[KROK 3] Gotuj:" in steps_text
        assert "[KROK 4] Podaj danie:" in steps_text
        
        # Sprawdz stopke
        assert "SMACZNEGO!" in steps_text
    
    def test_pizza_has_all_steps(self, pizza):
        """Test czy przepis na pizze ma wszystkie kroki"""
        result = pizza.prepare()
        steps_text = "\n".join(result["steps"])
        
        assert "PRZEPIS: Pizza Margherita" in steps_text
        assert "[KROK 1] Zbierz skladniki:" in steps_text
        assert "[KROK 2] Przygotuj skladniki:" in steps_text
        assert "[KROK 3] Gotuj:" in steps_text
        assert "[KROK 4] Podaj danie:" in steps_text
        assert "SMACZNEGO!" in steps_text
    
    def test_salad_has_all_steps(self, salad):
        """Test czy przepis na salatke ma wszystkie kroki"""
        result = salad.prepare()
        steps_text = "\n".join(result["steps"])
        
        assert "PRZEPIS: Salatka Grecka" in steps_text
        assert "[KROK 1] Zbierz skladniki:" in steps_text
        assert "[KROK 2] Przygotuj skladniki:" in steps_text
        assert "[KROK 3] Gotuj:" in steps_text  # Dla salatki to mieszanie
        assert "[KROK 4] Podaj danie:" in steps_text
        assert "SMACZNEGO!" in steps_text
    
    def test_soup_has_all_steps(self, soup):
        """Test czy przepis na zupe ma wszystkie kroki"""
        result = soup.prepare()
        steps_text = "\n".join(result["steps"])
        
        assert "PRZEPIS: Zupa Pomidorowa" in steps_text
        assert "[KROK 1] Zbierz skladniki:" in steps_text
        assert "[KROK 2] Przygotuj skladniki:" in steps_text
        assert "[KROK 3] Gotuj:" in steps_text
        assert "[KROK 4] Podaj danie:" in steps_text
        assert "SMACZNEGO!" in steps_text
    
    def test_pasta_specific_ingredients(self, pasta):
        """Test czy makaron ma wlasciwe skladniki"""
        result = pasta.prepare()
        steps_text = "\n".join(result["steps"])
        
        assert "Makaron spaghetti 250g" in steps_text
        assert "Mielone mieso 300g" in steps_text
        assert "Sos pomidorowy 400ml" in steps_text
    
    def test_pizza_specific_ingredients(self, pizza):
        """Test czy pizza ma wlasciwe skladniki"""
        result = pizza.prepare()
        steps_text = "\n".join(result["steps"])
        
        assert "Maka 300g" in steps_text
        assert "Mozzarella 200g" in steps_text
        assert "Bazylia" in steps_text
    
    def test_salad_specific_ingredients(self, salad):
        """Test czy salatka ma wlasciwe skladniki"""
        result = salad.prepare()
        steps_text = "\n".join(result["steps"])
        
        assert "Pomidor 3 szt" in steps_text
        assert "Feta 150g" in steps_text
        assert "Oliwki 100g" in steps_text
    
    def test_soup_specific_ingredients(self, soup):
        """Test czy zupa ma wlasciwe skladniki"""
        result = soup.prepare()
        steps_text = "\n".join(result["steps"])
        
        assert "Pomidory 1kg" in steps_text
        assert "Bulion 1l" in steps_text
        assert "Smietanka 200ml" in steps_text
    
    def test_pasta_cooking_instructions(self, pasta):
        """Test czy makaron ma wlasciwe instrukcje gotowania"""
        result = pasta.prepare()
        steps_text = "\n".join(result["steps"])
        
        assert "Zagotuj wode z sola" in steps_text
        assert "Wrzuc makaron, gotuj 10 min" in steps_text
        assert "Dodaj mieso" in steps_text
    
    def test_pizza_cooking_instructions(self, pizza):
        """Test czy pizza ma wlasciwe instrukcje pieczenia"""
        result = pizza.prepare()
        steps_text = "\n".join(result["steps"])
        
        assert "Nagrzej piekarnik do 220" in steps_text
        assert "Piecz 15 min" in steps_text
        assert "Rozwałkuj ciasto" in steps_text
    
    def test_salad_no_cooking(self, salad):
        """Test czy salatka nie wymaga gotowania"""
        result = salad.prepare()
        assert result["cook_time"] == 0
        
        steps_text = "\n".join(result["steps"])
        assert "Wymieszaj warzywa w misce" in steps_text
    
    def test_soup_cooking_instructions(self, soup):
        """Test czy zupa ma wlasciwe instrukcje gotowania"""
        result = soup.prepare()
        steps_text = "\n".join(result["steps"])
        
        assert "Zalej bulionem" in steps_text
        assert "Zmiksuj" in steps_text
        assert "Dodaj smietanke i makaron" in steps_text
    
    def test_pasta_serving_instructions(self, pasta):
        """Test instrukcji podawania makaronu"""
        result = pasta.prepare()
        steps_text = "\n".join(result["steps"])
        
        assert "Odcedz makaron" in steps_text
        assert "Polej sosem" in steps_text
        assert "Posyp parmezanem" in steps_text
    
    def test_pizza_serving_instructions(self, pizza):
        """Test instrukcji podawania pizzy"""
        result = pizza.prepare()
        steps_text = "\n".join(result["steps"])
        
        assert "Wyjmij z piekarnika" in steps_text
        assert "Pokroj na kawalki" in steps_text
        assert "Dodaj swieża bazylie" in steps_text
    
    def test_all_recipes_have_consistent_structure(self, pasta, pizza, salad, soup):
        """Test czy wszystkie przepisy maja spojna strukture"""
        recipes = [pasta, pizza, salad, soup]
        
        for recipe in recipes:
            result = recipe.prepare()
            steps = result["steps"]
            
            # Kazdy przepis musi miec te same sekcje
            steps_text = "\n".join(steps)
            assert "[KROK 1]" in steps_text
            assert "[KROK 2]" in steps_text
            assert "[KROK 3]" in steps_text
            assert "[KROK 4]" in steps_text
            assert "SMACZNEGO!" in steps_text
            
            # Sprawdz czy total_time jest poprawny
            assert result["total_time"] == result["prep_time"] + result["cook_time"]
    
    def test_recipe_returns_steps_list(self, pasta):
        """Test czy przepis zwraca liste krokow"""
        result = pasta.prepare()
        assert "steps" in result
        assert isinstance(result["steps"], list)
        assert len(result["steps"]) > 0
    
    def test_all_recipes_print_output(self, pasta, pizza, salad, soup, capsys):
        """Test czy wszystkie przepisy drukuja output"""
        recipes = [pasta, pizza, salad, soup]
        
        for recipe in recipes:
            recipe.prepare()
            captured = capsys.readouterr()
            assert len(captured.out) > 0
            assert "PRZEPIS:" in captured.out
