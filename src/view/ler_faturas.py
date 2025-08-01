import json
from src.model.vertex_client import ModelVertex
from src.utils.gerencia_arquivos import MoverArquivos, Utils
import os

modelo = ModelVertex()
controle_pdf = MoverArquivos()
utils = Utils()


class LerFaturas:
  def __init__(self):
    self.lista_faturas = []
    self.pasta_nao_lidos = utils.pasta_nao_lidos
    self.pasta_lidos = utils.pasta_lidos

  def ler_faturas(self):

    arquivos = os.listdir(self.pasta_nao_lidos)  
    for i in arquivos:
      resposta = json.loads(modelo.chama_modelo(fr"{self.pasta_nao_lidos}\{i}"))
      resposta.update({"ARQUIVO":i})
      if len(resposta['COD BARRAS']) < 30:
        resposta.update({"COD BARRAS":"Não encontrado"})
      controle_pdf.mover_pdf(i)
      self.lista_faturas.append(resposta)
    return self.lista_faturas
  
  
