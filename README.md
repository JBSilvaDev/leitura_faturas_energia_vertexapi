# Leitura de Faturas de Energia com Vertex API

Este projeto automatiza a leitura de faturas de energia em PDF, extraindo informações relevantes com auxílio da Vertex AI (Gemini), e exporta os dados para uma planilha Excel. O fluxo segue o padrão MVC (Model-View-Controller) para facilitar manutenção e expansão.
Verifique se o CLI do google esta instalado na maquina e devidamene configurado na conta GCP
Rode comando:
```bash
gcloud auth application-default login
```

## 📁 Estrutura de Pastas

```
data/
  export_excel/         # Planilhas Excel geradas
  pdfs_lidos/           # PDFs já processados
  pdfs_nao_lidos/       # PDFs a serem processados

src/
  controller/
    controlador_pdfs.py # Lógica de orquestração do fluxo
  model/
    fatura.py           # Schema/modelo de dados das faturas
    pdf_leitor.py       # Extração de texto dos PDFs
    vertex_client.py    # Integração com Vertex AI (Gemini)
    converte_excel.py   # Exportação para Excel
  utils/
    gerencia_arquivos.py# Utilitários de arquivos e variáveis de ambiente
  view/
    ler_faturas.py      # Interface de serviços para o main

main.py                 # Ponto de entrada do sistema
```

## 🚀 Como Usar

1. **Pré-requisitos**
   - Python 3.8+
   - Dependências do projeto (instale com `pip install -r requirements.txt`)
   - Variáveis de ambiente configuradas em um arquivo `.env`:
     ```
     CAMINHO=<caminho absoluto do projeto>
     PROJETO_GCP=<nome do projeto GCP>
     ```

2. **Adicione os PDFs**
   - Coloque os arquivos PDF a serem processados na pasta `data/pdfs_nao_lidos/`.
    - Há dois arquivos de exemplo da distribuidora de energia Energisa, que podem ser utilizados para testes.

3. **Execute o Projeto**
   ```bash
   python main.py
   ```

4. **Resultados**
   - Os PDFs processados serão movidos para `data/pdfs_lidos/`.
   - O arquivo Excel será gerado em `data/export_excel/faturas.xlsx`.

## 🛠️ Principais Funcionalidades

- **Extração automática de dados** de faturas PDF usando IA generativa (Vertex AI Gemini).
- **Exportação dos dados** para planilha Excel.
- **Organização automática dos arquivos** processados.

## 🧩 Arquitetura

- **Model:** Lida com dados, extração de texto e integração com IA.
- **View:** Expõe serviços para o ponto de entrada.
- **Controller:** Orquestra o fluxo de processamento.
- **Utils:** Funções auxiliares para manipulação de arquivos e configuração.


## 📚 Licença

Este projeto é de uso interno e educacional. Consulte o responsável pelo projeto para informações sobre uso e distribuição.

---
Desenvolvido por JB Silva