import xml.etree.ElementTree as xml
from typing import List, Dict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path: str) -> List[Dict]:
        if path.endswith('.xml'):
            return [
                {line.tag: line.text for line in product}
                for product in xml.parse(path).getroot()
            ]

        raise ValueError('Arquivo inválido')
