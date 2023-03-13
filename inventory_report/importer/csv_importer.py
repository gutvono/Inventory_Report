import csv
from typing import List, Dict
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path: str) -> List[Dict]:
        with open(path, mode='r') as data:
            if path.endswith('.csv'):
                return [product for product in csv.DictReader(data)]

        raise ValueError('Arquivo inválido')
