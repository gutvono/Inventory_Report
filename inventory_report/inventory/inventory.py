from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    # Recebe o caminho do arquivo a ser lido (que pode ser .csv, .json ou .xml)
    # e retorna os dados.
    @staticmethod
    def get_file_extension(path: str) -> str:
        if path.endswith('.csv'):
            return CsvImporter.import_data(path)
        elif path.endswith('.json'):
            return JsonImporter.import_data(path)
        elif path.endswith('.xml'):
            return XmlImporter.import_data(path)

    # Recebe o caminho do arquivo e o tipo de relatório que deve ser gerado.
    @staticmethod
    def import_data(path: str, type: str) -> str:
        products = Inventory.get_file_extension(path)
        if type == 'simples':
            return SimpleReport.generate(products)
        return CompleteReport.generate(products)
