from limite.tela_tamanho import TelaTamanho
from entidade.tamanho import Tamanho

class ControladorTamanhos():
  # Fazer lançamento e tratamento de exceções, ao invés de apenas mostrar mensagem na tela.
  def __init__(self, controlador_sistema):
    self.__tamanhos = []
    self.__controlador_sistema = controlador_sistema
    self.__tela_tamanho = TelaTamanho()

  def pega_tamanho_por_codigo(self, codigo: int):
    for tamanho in self.__tamanhos:
      if(tamanho.codigo == codigo):
        return tamanho
    return None

  def incluir_tamanho(self):
    dados_tamanho = self.__tela_tamanho.pega_dados_tamanho()
    tamanho = Tamanho(dados_tamanho["descricao"], dados_tamanho["codigo"])
    self.__tamanhos.append(tamanho)

  def alterar_tamanho(self):
    self.lista_tamanho()
    codigo_tamanho = self.__tela_tamanho.seleciona_tamanho()
    tamanho = self.pega_tamanho_por_codigo(codigo_tamanho)

    if(tamanho is not None):
      novos_dados_tamanho = self.__tela_tamanho.pega_dados_tamanho()
      tamanho.descricao = novos_dados_tamanho["descricao"]
      tamanho.codigo = novos_dados_tamanho["codigo"]
      self.lista_tamanho()
    else:
      self.__tela_tamanho.mostra_mensagem("ATENCAO: Tamanho não existente")

  # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_tamanho(self):
    for tamanho in self.__tamanhos:
      self.__tela_tamanho.mostra_tamanho({"descricao": tamanho.descricao, "codigo": tamanho.codigo})

  def excluir_tamanho(self):
    self.lista_tamanho()
    codigo_tamanho = self.__tela_tamanho.seleciona_tamanho()
    tamanho = self.pega_tamanho_por_codigo(codigo_tamanho)

    if(tamanho is not None):
      self.__tamanhos.remove(tamanho)
      self.lista_tamanho()
    else:
      self.__tela_tamanho.mostra_mensagem("ATENCAO: Tamanho não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_tamanho, 2: self.alterar_tamanho, 3: self.lista_tamanho, 4: self.excluir_tamanho, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_tamanho.tela_opcoes()]()
