Verificar se o CLI do google esta instalado na maquina e devidamene configurado na conta GCP
Rodar comando:
```bash
gcloud auth application-default login
```

api-gemini/
│
├── data/
│   ├── faturas_pendentes/
│   └── faturas_processadas/
│
├── src/
│   ├── model/
│   │   ├── __init__.py
│   │   ├── fatura.py            # Classe(s) para representar fatura e lógica de extração
│   │   └── pdf_extractor.py     # Função/classe para extrair texto do PDF
          

│   │
│   ├── view/
│   │   ├── __init__.py
│   │   └── main.py              # Interface: notebook, CLI ou API
│   │
│   ├── controller/
│   │   ├── __init__.py
│   │   └── fatura_controller.py # Orquestra o fluxo entre model e view
│   │
│   └── utils/
│       ├── __init__.py
│       └── file_manager.py      # Funções para mover/gerenciar arquivos
│
├── requirements.txt
├── README.md
└── .gitignore

src/
├── model/
│   ├── __init__.py
│   ├── fatura.py              # Estruturas de dados (dataclasses)
│   ├── pdf_extractor.py       # Funções para extrair texto do PDF
│   └── vertex_client.py       # Classe/funções para interação com a API Vertex/Gemini
│
├── view/
│   └── main.py                # Interface com o usuário
│
├── controller/
│   └── fatura_controller.py   # Orquestra o fluxo entre view e model
│
└── utils/
    └── file_manager.py        # Funções auxiliares