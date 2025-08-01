import vertexai
from vertexai.generative_models import GenerativeModel, GenerationConfig
from src.model.fatura import Faturas
from src.model.pdf_leitor import ExtratorPDF
from src.utils.gerencia_arquivos import Utils

FORMATO_RESPOSTA = Faturas().modelo_resposta()
SCHEMA_RESPOSTA = Faturas().schema_resposta()
utils = Utils()

class ModelVertex:
  def __init__(self):
    # Inicializa o Vertex AI
    vertexai.init(project=utils.projeto_gcp, location="us-central1")
    self.model: GenerativeModel
    self.config: GenerationConfig
    self.pdf_text = None
    self.contents = []

  def criar_modelo(self):
    # Carrega o modelo Gemini
    self.model = GenerativeModel("gemini-1.5-flash-002", system_instruction=f"""
                        Você é um analista responsável por catalogar arquivos, extraindo de forma detalhada todo o seu conteúdo. Formate a resposta com um único JSON, acessível via json.loads python. Normalmente COD BARRAS são inicados em '341' ou 836
                        {FORMATO_RESPOSTA}
                        Se alguma informação não for encontrada, preencha com 'não encontrado'. Para o campo IDENTIFICADOR, caso haja mais de um disponível, traga todos separados por ';'""")
    self.config = GenerationConfig(
      temperature=0.1,
      max_output_tokens=8192,
      response_mime_type="application/json",
      response_schema= SCHEMA_RESPOSTA
    )
    self.contents = [
      f"Resuma o documento, a resposta com um único JSON, acessível via json.loads python",
      self.pdf_text 
  ]
    
  def chama_modelo(self, arquivo_pdf):
    self.pdf_text = ExtratorPDF().extrair_texto_pdf(arquivo_pdf)
    self.criar_modelo()
    self.response = self.model.generate_content(self.contents, generation_config=self.config)

    return self.response.text
