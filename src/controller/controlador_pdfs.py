from src.model.converte_excel import ExportExcel
from src.utils.gerencia_arquivos import Utils
import os
import json
from src.model.vertex_client import ModelVertex
from src.utils.gerencia_arquivos import MoverArquivos, Utils

modelo = ModelVertex()
controle_pdf = MoverArquivos()
utils = Utils()


class ControladorFaturas:
    def __init__(self):
        self.lista = []
        self.nao_lidos = utils.pasta_nao_lidos
        self.lidos = utils.pasta_lidos

    def processar_faturas(self):
        arquivos_pdf = os.listdir(self.nao_lidos) 
        for i in arquivos_pdf:
            resposta = json.loads(modelo.chama_modelo(fr"{self.nao_lidos}\{i}"))
            resposta.update({"ARQUIVO":i})
            if len(resposta['COD BARRAS']) < 30:
                resposta.update({"COD BARRAS":"Não encontrado"})
            controle_pdf.mover_pdf(i)
            self.lista.append(resposta)
        return self.lista


    def exportar_faturas_para_excel(self, faturas):
        exportar_excel = ExportExcel(faturas)
        exportar_excel.exportar_excel()