from abc import ABC, abstractmethod
from typing import List, Dict

class Recipe(ABC):
    def __init__(self, name: str, prep_time: int, cook_time: int):
        self.name = name
        self.prep_time = prep_time
        self.cook_time = cook_time

    def prepare(self):
        steps = []

        self.header(steps)
        self.gather_ingredients(steps)
        self.prepare_ingredients(steps)
        self.cook(steps)
        self.serve(steps)
        self.footer(steps)

        result = "\n".join(steps)
        print(result)

        return {
            "name": self.name,
            "prep_time": self.prep_time,
            "cook_time": self.cook_time,
            "total_time": self.prep_time + self.cook_time,
            "steps": steps
        }

    def header(self, steps: List[str]):
        steps.append("=" * 50)
        steps.append(f"PRZEPIS: {self.name}")
        steps.append(f"Czas przygotowania: {self.prep_time} min")
        steps.append(f"Czas gotowania: {self.cook_time} min")
        steps.append("=" * 50)

    def footer(self, steps: List[str]):
        steps.append("\n" + "=" * 50)
        steps.append("SMACZNEGO!")
        steps.append("=" * 50)

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