from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):

    def inventory_companies(products):
        comp_str = ""
        companies = [product["nome_da_empresa"] for product in products]
        company_common = Counter(companies)
        for company, count in company_common.items():
            comp_str += f"- {company}: {count}\n"
        return comp_str

    @staticmethod
    def generate(products: list[dict]):
        return (
            f"Data de fabricação mais antiga: "
            f"{min(CompleteReport.oldest_product_generator(products))}\n"
            f"Data de validade mais próxima: "
            f"{CompleteReport.closest_valid_date_generator(products)}\n"
            f"Empresa com mais produtos: "
            f"{CompleteReport.most_common_company_generator(products)}\n"
            f"Produtos estocados por empresa:\n"
            f"{CompleteReport.inventory_companies(products)}"
        )
