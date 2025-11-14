from abc import ABC, abstractmethod
from typing import Dict

class Recipe(ABC):

    def prepare(self) -> Dict:

        steps = []

        steps.append(self.header())
        steps.append(self.gather_ingredients())
        steps.append(self.prepare_ingredients())
        steps.append(self.cook())
        steps.append(self.serve())
        steps.append(self.footer())

        result = "\n".join(steps)
        print(result)
        
        return {
            "name": self.get_name(),
            "prep_time": self.get_prep_time(),
            "cook_time": self.get_cook_time(),
            "total_time": self.get_prep_time() + self.get_cook_time(),
            "steps": steps
        }
    
    def header(self) -> str:
        steps = []
        steps.append("=" * 50)
        steps.append(f"PRZEPIS: {self.get_name()}")
        steps.append(f"Czas przygotowania: {self.get_prep_time()} min")
        steps.append(f"Czas gotowania: {self.get_cook_time()} min")
        steps.append("=" * 50)
        return "\n".join(steps)
    
    def footer(self) -> str:
        steps = []
        steps.append("\n" + "=" * 50)
        steps.append("SMACZNEGO!")
        steps.append("=" * 50)
        return "\n".join(steps)

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_prep_time(self) -> int:
        pass

    @abstractmethod
    def get_cook_time(self) -> int:
        pass

    @abstractmethod
    def gather_ingredients(self) -> str:
        pass

    @abstractmethod
    def prepare_ingredients(self) -> str:
        pass

    @abstractmethod
    def cook(self) -> str:
        pass

    @abstractmethod
    def serve(self) -> str:
        pass

