import json
from src.model.vertex_client import ModelVertex
from src.utils.gerencia_arquivos import MoverArquivos, CAMINHO_RAIZ
import os

modelo = ModelVertex()
pastas_pdfs = MoverArquivos()


class LerFaturas:
  def __init__(self):
    self.lista_faturas = []

  def ler_faturas(self, caminho):

    self.pasta_nao_lidos = fr"{caminho}\pdfs_nao_lidos"
    self.pasta_lidos = fr"{caminho}\pdfs_lidos"
    arquivos = os.listdir(self.pasta_nao_lidos)  

    for i in arquivos:
      resposta = json.loads(modelo.chama_modelo(fr"{self.pasta_nao_lidos}\{i}"))
      resposta.update({"ARQUIVO":i})
      if len(resposta['COD BARRAS']) < 30:
        resposta.update({"COD BARRAS":"Não encontrado"})
      pastas_pdfs.mover_pdf(self.pasta_nao_lidos, self.pasta_lidos, i)
      self.lista_faturas.append(resposta)
    return self.lista_faturas
