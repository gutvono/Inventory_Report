import xml.etree.ElementTree as xml
from typing import List, Dict
from importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def get_file_content(path: str) -> List[Dict]:
        with open(path, mode='r'):
            if path.endswith('.xml'):
                return [
                    {line.tag: line.text for line in product}
                    for product in xml.parse(path).getroot()
                ]

        raise ValueError('Invalid file format')
