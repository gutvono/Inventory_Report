import csv
from typing import List, Dict
from importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def get_file_content(path: str) -> List[Dict]:
        with open(path, mode='r') as data:
            if path.endswith('.csv'):
                return [product for product in csv.DictReader(data)]

        raise TypeError('Invalid file format')
