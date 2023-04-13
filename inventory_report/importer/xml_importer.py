from .importer import Importer
# pesquisa feita no site https://python-guide-pt-br.readthedocs.io
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, pathFile: str):
        if not pathFile.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        try:
            with open(pathFile) as path:
                newData = xmltodict.parse(path.read())
                # lendo o arquivo inventory.xml
                data_format = newData["dataset"]["record"]
        except FileNotFoundError as err:
            print("Arquivo não encontrado")
            print(err)
        return data_format
