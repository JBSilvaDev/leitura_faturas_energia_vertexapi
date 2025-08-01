import os
import shutil
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

CAMINHO_RAIZ = os.getenv("CAMINHO")


class MoverArquivos:
    def __init__(self):
        self.caminho_origem = ""
        self.caminho_destino = ""
        self.arquivo = ""

    def mover_pdf(self, origem, destino, arquivo):
      self.caminho_origem = Path(fr"{CAMINHO_RAIZ}\data\{origem}")
      self.caminho_destino = Path(fr"{CAMINHO_RAIZ}\data\{destino}")
      self.arquivo = Path(fr"{origem}\{arquivo}")
      shutil.move(self.arquivo, destino)

