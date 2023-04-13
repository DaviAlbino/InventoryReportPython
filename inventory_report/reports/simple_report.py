from datetime import datetime


class SimpleReport:

    def oldest_product_generator(products):
        oldest_product = [
            datetime.strptime(
                    product["data_de_fabricacao"], "%Y-%m-%d"
                ).date() for product in products
            ]
        return oldest_product

    def closest_valid_date_generator(products):
        current_date = datetime.now().date()
        correct_dates = [
            datetime.strptime(
                product["data_de_validade"], "%Y-%m-%d"
            ).date() for product in products
            if datetime.strptime(
                product["data_de_validade"], "%Y-%m-%d"
            ).date() >= current_date
        ]
        if not correct_dates:
            closest_date_str = "N/A"
        else:
            closest_correct_date = min(correct_dates)
            closest_date_str = closest_correct_date.strftime("%Y-%m-%d")
        return closest_date_str

    def most_common_company_generator(products):
        companies_dict = {}
        for product in products:
            company = product["nome_da_empresa"]
            if company in companies_dict:
                companies_dict[company] += 1
            else:
                companies_dict[company] = 1
        most_found_company = None
        higher_company = 0
        for company, count in companies_dict.items():
            if count > higher_company:
                most_found_company = company
                higher_company = count
        return most_found_company

    @staticmethod
    def generate(products: list[dict]):
        return (
            f"Data de fabricação mais antiga: "
            f"{min(SimpleReport.oldest_product_generator(products))}\n"
            f"Data de validade mais próxima: "
            f"{SimpleReport.closest_valid_date_generator(products)}\n"
            f"Empresa com mais produtos: "
            f"{SimpleReport.most_common_company_generator(products)}"
        )
