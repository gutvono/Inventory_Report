from abc import ABC, abstractmethod
from typing import List, Dict


class Importer(ABC):
    @staticmethod
    @abstractmethod
    def import_data(self, path: str) -> List[Dict]:
        ...
