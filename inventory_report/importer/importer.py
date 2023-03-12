from abc import ABC, abstractmethod
from typing import List, Dict


class Importer(ABC):
    @staticmethod
    @abstractmethod
    def get_file_content(self, path: str) -> List[Dict]:
        ...
