from src.model.pdf_leitor import ExtratorPDF
from src.utils.gerencia_arquivos import MoverArquivos


class ControladorPDFs:
    def __init__(self):
        self.extrator_pdf = ExtratorPDF()
        self.mover_arquivos = MoverArquivos()