import json
from typing import List, Dict
from importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def get_file_content(path: str) -> List[Dict]:
        with open(path, mode='r') as data:
            if path.endswith('.json'):
                return json.load(data)

        raise TypeError('Invalid file format')
