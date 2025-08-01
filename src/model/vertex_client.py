import vertexai
from google.cloud import aiplatform
from vertexai.generative_models import GenerativeModel, GenerationConfig
import PyPDF2
from pathlib import Path
import os
import pandas as pd
import json
import shutil

from src.model.fatura import Faturas

FORMATO_RESPOSTA = Faturas().modelo_resposta()
CAMINHO_RAIZ = os.getenv("CAMINHO")
PROJETO_GCP = os.getenv("PROJETO_GCP")

class ModelVertex:
  def __init__(self):
    # Inicializa o Vertex AI
    vertexai.init(project=PROJETO_GCP, location="us-central1")
    # Carrega o modelo Gemini
    self.model = GenerativeModel("gemini-1.5-flash-002", system_instruction=f"""
                        Você é um analista responsável por catalogar arquivos, extraindo de forma detalhada todo o seu conteúdo. Formate a resposta com um único JSON, acessível via json.loads python.
                        {FORMATO_RESPOSTA}
                        Se alguma informação não for encontrada, preencha com 'não encontrado'. Para o campo IDENTIFICADOR, caso haja mais de um disponível, traga todos separados por ';'""")

