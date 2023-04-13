from .importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, pathFile: str):
        if not pathFile.endswith(".csv"):
            raise ValueError("Arquivo Inválido")

        pathList = []
        try:
            with open(pathFile) as path:
                newData = list(csv.DictReader(path))
                pathList = newData
        except FileNotFoundError as err:
            print("Arquivo não encontrado")
            print(err)
        return pathList
