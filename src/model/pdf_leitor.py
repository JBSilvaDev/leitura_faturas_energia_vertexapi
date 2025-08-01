import PyPDF2

class ExtratorPDF:
    def __init__(self):
        pass

    def extrair_texto_pdf(self, file_path):
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            if len(text) == 0:
                return """Não encontrado texto no arquivo PDF"""
            return text
