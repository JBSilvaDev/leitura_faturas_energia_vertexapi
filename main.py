
from src.model.converte_excel import ExportExcel
from src.view.ler_faturas import LerFaturas
import os
from dotenv import load_dotenv

load_dotenv()
CAMINHO_RAIZ = os.getenv("CAMINHO")
pasta_data = fr"{CAMINHO_RAIZ}\data"
pasta_nao_lidos = fr"{pasta_data}\pdfs_nao_lidos"
pasta_lidos = fr"{pasta_data}\pdfs_lidos"


def main():
    ler_faturas = LerFaturas(pasta_nao_lidos, pasta_lidos)
    faturas = ler_faturas.ler_faturas(pasta_data)
    print(faturas)
    exportar_excel = ExportExcel(faturas, pasta_data)
    exportar_excel.exportar_excel()


if __name__ == "__main__":
    main()