from src.controller.controlador_pdfs import ControladorFaturas
from src.model.vertex_client import ModelVertex
from src.utils.gerencia_arquivos import MoverArquivos, Utils


modelo = ModelVertex()
mover = MoverArquivos()
utils = Utils()
controle = ControladorFaturas()



class ServicosPDFs:
  def __init__(self):
    self.lista_faturas = []
    self.pasta_nao_lidos = utils.pasta_nao_lidos
    self.pasta_lidos = utils.pasta_lidos

  def ler_faturas(self):
    self.lista_faturas = controle.processar_faturas()
    return self.lista_faturas
  
  def exportar_excel(self, faturas):
    controle.exportar_faturas_para_excel(faturas)
    return faturas
  
  
