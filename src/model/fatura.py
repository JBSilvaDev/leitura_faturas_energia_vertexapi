class Faturas:
  def __init__(self) -> None:
    
    pass

  def data_dict(self):
    """
    Retorna um dicionário com as chaves e valores esperados para a resposta da API.
    """
    return {
      "ARQUIVO":"nome do arquivo pdf de onde trouxe as informações",
      "NF":	"numero da nota fiscal, normalmente apos o texto 'NOTA FISCAL Nº:' e proximo a data de emissão",
      "EMISSAO":	"data de emissao (formato dd.mm.yyyy)",
      "VALOR":	"valor final a ser pago",
      "VENCIMENTO":	"data de vencimento (formato dd.mm.yyyy)",
      "COD BARRAS":	"código de barras do boleto Exemplo: '00000000000-0 00000000000-0 00000000000-0 00000000000-0' ou '00000.00000 00000.000000 00000.000000 0 00000000000000' ou '00000000000000000000000000000000000000000000000'",
      "DISTRIBUIDORA": "nome da distribuidora de energia",
      "CLIENTE_NOME":"nome do cliente EX: Suzano S.A",
      "CNPJ_DISTR": "cnpj do distribuidor de energia",
      "CNPJ_CLIENT": "cnpj do cliente",
      "IDENTIFICADOR":"meu codigo/instalacao/contrato/uc/unidade consumidora/codigo cliente/seu codigo (caso exista mais de um, separar por ';')"
    }