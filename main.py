
from src.view.ler_faturas import LerFaturas
import os
from dotenv import load_dotenv

load_dotenv()
CAMINHO_RAIZ = os.getenv("CAMINHO")
pasta_nao_lidas = fr"{CAMINHO_RAIZ}\data"


def main():
    ler_faturas = LerFaturas()
    faturas = ler_faturas.ler_faturas(caminho=pasta_nao_lidas)
    print(faturas)


if __name__ == "__main__":
    main()