from abc import ABC, abstractmethod
from typing import List, Dict


class Importer(ABC):
    # Implementar o padrão de projeto Strategy, dividindo a complexidade
    # para cada formato de arquivo.
    @staticmethod
    @abstractmethod
    def import_data(self, path: str) -> List[Dict]:
        ...
