
from src.model.converte_excel import ExportExcel
from src.utils.gerencia_arquivos import Utils
from src.view.ler_faturas import LerFaturas

utils = Utils()


def main():
    ler_faturas = LerFaturas()
    faturas = ler_faturas.ler_faturas()
    print(faturas)
    exportar_excel = ExportExcel(faturas)
    exportar_excel.exportar_excel()


if __name__ == "__main__":
    main()