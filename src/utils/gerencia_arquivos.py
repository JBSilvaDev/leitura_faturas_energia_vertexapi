import os
import shutil
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Utils:
    def __init__(self):
      self.caminho_raiz = os.getenv("CAMINHO")
      self.projeto_gcp = os.getenv("PROJETO_GCP")
      self.pasta_data = fr"{self.caminho_raiz}\data"
      self.pasta_nao_lidos = fr"{self.pasta_data}\pdfs_nao_lidos"
      self.pasta_lidos = fr"{self.pasta_data}\pdfs_lidos"
      self.pasta_excel = fr"{self.pasta_data}\export_excel"


class MoverArquivos:
    def __init__(self):
      self.utils = Utils() 
      self.arquivo = ""

    def mover_pdf(self, arquivo):
      self.arquivo = Path(fr"{self.utils.pasta_nao_lidos}\{arquivo}")
      shutil.move(self.arquivo, self.utils.pasta_lidos)

