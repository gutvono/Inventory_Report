from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xml.etree.ElementTree as xml


class Inventory:
    @staticmethod
    def get_file_extension(path: str) -> str:
        with open(path, mode='r') as data:
            if path.endswith('.csv'):
                return [product for product in csv.DictReader(data)]
            elif path.endswith('.json'):
                return json.load(data)
            elif path.endswith('.xml'):
                return [
                    {line.tag: line.text for line in product}
                    for product in xml.parse(path).getroot()
                ]

    @staticmethod
    def import_data(path: str, type: str) -> str:
        products = Inventory.get_file_extension(path)
        if type == 'simples':
            return SimpleReport.generate(products)
        return CompleteReport.generate(products)