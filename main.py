
from src.model.converte_excel import ExportExcel
from src.view.ler_faturas import ServicosPDFs





def main():
    servicos = ServicosPDFs()
    faturas = servicos.ler_faturas()
    servicos.exportar_excel(faturas)


if __name__ == "__main__":
    main()