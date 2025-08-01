import os
import shutil
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

CAMINHO_RAIZ = os.getenv("CAMINHO")


class MoverArquivos:
    def __init__(self, caminho_origem, caminho_destino, arquivo):
        self.caminho_origem = caminho_origem
        self.caminho_destino = caminho_destino
        self.arquivo = arquivo

    def mover_pdf(self):
      origem = Path(fr"{CAMINHO_RAIZ}\data\{self.caminho_origem}")
      destino = Path(fr"{CAMINHO_RAIZ}\data\{self.caminho_destino}")
      arquivo = Path(fr"{origem}\{self.arquivo}")
      shutil.move(arquivo, destino)