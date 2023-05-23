import json
from typing import List, Dict
from inventory_report.importer.importer import Importer


# Classe responsável por importar o arquivo .json e retornar os dados
# em uma lista de dicionários pronto para serem manipulados.
class JsonImporter(Importer):
    @staticmethod
    def import_data(path: str) -> List[Dict]:
        with open(path, mode='r') as data:
            if path.endswith('.json'):
                return json.load(data)

        raise ValueError('Arquivo inválido')
