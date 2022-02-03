from limite.tela_cor import TelaCor
from entidade.cor import Cor

class ControladorCores():
  # Fazer lançamento e tratamento de exceções, ao invés de apenas mostrar mensagem na tela.
  def __init__(self, controlador_sistema):
    self.__cores = []
    self.__controlador_sistema = controlador_sistema
    self.__tela_cor = TelaCor()

  def pega_cor_por_codigo(self, codigo: int):
    for cor in self.__cores:
      if(cor.codigo == codigo):
        return cor
    return None

  def incluir_cor(self):
    dados_cor = self.__tela_cor.pega_dados_cor()
    cor = Cor(dados_cor["nome"], dados_cor["codigo"])
    self.__cores.append(cor)

  def alterar_cor(self):
    self.lista_cor()
    codigo_cor = self.__tela_cor.seleciona_cor()
    cor = self.pega_cor_por_codigo(codigo_cor)

    if(cor is not None):
      novos_dados_cor = self.__tela_cor.pega_dados_cor()
      cor.nome = novos_dados_cor["nome"]
      cor.codigo = novos_dados_cor["codigo"]
      self.lista_cor()
    else:
      self.__tela_cor.mostra_mensagem("ATENCAO: Cor não existente")

  # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_cor(self):
    for cor in self.__cores:
      self.__tela_cor.mostra_cor({"nome": cor.nome, "codigo": cor.codigo})

  def excluir_cor(self):
    self.lista_cor()
    codigo_cor = self.__tela_cor.seleciona_cor()
    cor = self.pega_cor_por_codigo(codigo_cor)

    if(cor is not None):
      self.__cores.remove(cor)
      self.lista_cor()
    else:
      self.__tela_cor.mostra_mensagem("ATENCAO: Cor não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_cor, 2: self.alterar_cor, 3: self.lista_cor, 4: self.excluir_cor, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_cor.tela_opcoes()]()
