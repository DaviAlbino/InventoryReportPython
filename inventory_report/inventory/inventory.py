from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @staticmethod
    def import_Importer(path: str):

        if path.endswith(".csv"):
            data = CsvImporter.import_data(path)
            return data
        if path.endswith(".xml"):
            data = XmlImporter.import_data(path)
            return data

        if path.endswith(".json"):
            data = JsonImporter.import_data(path)
            return data

    @staticmethod
    def import_data(path: str, type: str):
        if type == "simples":
            importer_type = Inventory.import_Importer(path)
            return SimpleReport.generate(importer_type)

        if type == "completo":
            importer_type = Inventory.import_Importer(path)
            return CompleteReport.generate(importer_type)
