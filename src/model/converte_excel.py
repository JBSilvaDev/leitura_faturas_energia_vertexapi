import pandas as pd

class ExportExcel:
  def __init__(self, df_json, caminho):
    self.df = pd.DataFrame(df_json)
    self.caminho = caminho

  def exportar_excel(self):
    caminho_excel = f"{self.caminho}/faturas.xlsx"
    self.df.to_excel(caminho_excel, index=False)

