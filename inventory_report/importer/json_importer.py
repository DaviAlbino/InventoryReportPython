from .importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, pathFile: str):
        if not pathFile.endswith(".json"):
            raise ValueError("Arquivo inválido")

        try:
            with open(pathFile) as path:
                newData = path.read()
                load_json = json.loads(newData)
        except FileNotFoundError as err:
            print("Arquivo não encontrado")
            print(err)
        return load_json
