import pandas as pd

from src.utils.gerencia_arquivos import Utils

utils = Utils()

class ExportExcel:
  def __init__(self, df_json):
    self.df = pd.DataFrame(df_json)
    self.caminho = utils.pasta_excel

  def exportar_excel(self):
    caminho_excel = fr"{self.caminho}\faturas.xlsx"
    self.df.to_excel(caminho_excel, index=False)

