from inventory_report.reports.simple_report import SimpleReport
from typing import List, Dict


class CompleteReport:
    @staticmethod
    def generate(data: List[Dict]) -> str:
        simple_report = SimpleReport.generate(data)
        products_by_companies = {}

        for product in data:
            if product["nome_da_empresa"] in products_by_companies:
                products_by_companies[product["nome_da_empresa"]] += 1
            else:
                products_by_companies[product["nome_da_empresa"]] = 1

        companies = "\nProdutos estocados por empresa:\n"
        for company, quantity in products_by_companies.items():
            companies += f"- {company}: {quantity}\n"

        return (
            f"{simple_report}"
            f"{companies}"
        )
