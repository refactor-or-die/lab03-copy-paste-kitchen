from abc import ABC, abstractmethod
from typing import List, Dict


class Recipe(ABC):
    def __init__(self, name, prep_time, cook_time):
        self.name = name
        self.prep_time = prep_time
        self.cook_time = cook_time

    def _seperator(self, steps: List[str], newline=False):
        if newline:
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

        self._step_header(2, "Przygotuj skladniki", steps)
        self.prepare_ingredients(steps)

        self._step_header(3, "Gotuj", steps)
        self.cook(steps)

        self._step_header(4, "Podaj danie", steps)
        self.serve(steps)

        self._footer(steps)

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
