from datetime import date
from typing import List, Dict


# Classe responsável por gerar um relatório simples.
class SimpleReport:
    @staticmethod
    def generate(data: List[Dict]) -> str:
        oldest_manufacturing_date = str(date.max)
        nearest_expiration_date = str(date.max)
        today = str(date.today())
        counter = {}

        for product in data:
            if product["data_de_fabricacao"] < oldest_manufacturing_date:
                oldest_manufacturing_date = product["data_de_fabricacao"]

            if today <= product["data_de_validade"] < nearest_expiration_date:
                nearest_expiration_date = product["data_de_validade"]

            if product["nome_da_empresa"] in counter:
                counter[product["nome_da_empresa"]] += 1
            else:
                counter[product["nome_da_empresa"]] = 1

        most_commom_company = max(counter, key=counter.get)
        company_with_more_products = most_commom_company

        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
            f"Data de validade mais próxima: {nearest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )
