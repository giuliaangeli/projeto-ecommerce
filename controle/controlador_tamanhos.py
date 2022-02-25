from limite.tela_tamanho import TelaTamanho
from entidade.tamanho import Tamanho

class ControladorTamanhos():
  # Fazer lançamento e tratamento de exceções, ao invés de apenas mostrar mensagem na tela.
  def __init__(self, controlador_sistema):
    self.__tamanhos = []
    self.__controlador_sistema = controlador_sistema
    self.__tela_tamanho = TelaTamanho()

  def confere_tamanho_descricao(self, descricao):
    for tamanho in self.__tamanhos:
      if (tamanho.descricao == descricao):
        return tamanho
    return None

  def incluir_tamanho(self):
    dados_tamanho = self.__tela_tamanho.pega_dados_tamanho()
    nova_tamanho = self.confere_tamanho_descricao(dados_tamanho["descricao"])

    if nova_tamanho == None:
      tamanho = Tamanho(dados_tamanho["descricao"])
      self.__tamanhos.append(tamanho)
      self.__tela_tamanho.mostra_mensagem("ATENÇÃO: Tamanho foi selecionado com sucesso")
      return None
    self.__tela_tamanho.mostra_mensagem("ATENÇÃO: Esse tamanho já está cadastrado")

  def alterar_tamanho(self):
    self.__tela_tamanho.mostra_mensagem("ATENÇÃO: Digite a descrição do tamanho que você deseja alterar")
    tamanhoAntigo = input().upper()
    tamanhoAntigo = tamanhoAntigo.strip()
    self.__tela_tamanho.mostra_mensagem("ATENÇÃO: Digite a descrição do tamanho pelo qual você deseja substituir")
    tamanhoNovo = input().upper()
    tamanhoNovo = tamanhoNovo.strip()
    verefica1 = False
    verefica = False
    for tamanho in self.__tamanhos:
      if tamanho.descricao == tamanhoAntigo:
        verefica = True
      if tamanho.descricao == tamanhoNovo:
        verefica1 = True
        self.__tela_tamanho.mostra_mensagem("ATENÇÃO: O tamanho que você deseja alterar já se encontra na lista")
    if verefica == True and verefica1 != True:
      for tamanho in self.__tamanhos:
        if tamanho.descricao == tamanhoAntigo:
          self.__tela_tamanho.mostra_mensagem("ATENÇÃO: Tamanho alterado com suesso")
          tamanho.descricao = tamanhoNovo
    if verefica == False:
      self.__tela_tamanho.mostra_mensagem("ATENÇÃO: O trabalho que deseja alterar não se encontra na lista de cores")

  # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_tamanho(self):
    for tamanho in self.__tamanhos:
      self.__tela_tamanho.mostra_tamanho({"descricao": tamanho.descricao})

  def excluir_tamanho(self):
   descricao = self.__tela_tamanho.seleciona_tamanho()
    for tamanho in self.__tamanhos:
      if tamanho.descricao == descricao:
        self.__tamanhos.remove(tamanho)
        self.__tela_tamanho.mostra_mensagem("ATENÇÃO: Tamanho removido")
      else:
        self.__tela_tamanho.mostra_mensagem("ATENÇÃO: Esee tamanho não está cadastrado")
        
  def retornar_menu__produto(self, adm):
    self.__controlador_sistema.controlador_produtos.menu_incluir_produto(adm)

  def abre_tela(self, adm):
    lista_opcoes = {1: self.incluir_tamanho, 2: self.alterar_tamanho, 3: self.lista_tamanho, 4: self.excluir_tamanho, 5: self.retornar_menu__produto, 6: self.__controlador_sistema.abre_tela_inicial}

    continua = True
    while continua:
      opcao_escolhida = self.__tela_tamanho.tela_opcoes()
      if opcao_escolhida == 5:
        lista_opcoes[opcao_escolhida](adm)
      else:
        lista_opcoes[opcao_escolhida]()

  def instancia_tamanho(self):
    tamanho1 = Tamanho('P')
    tamanho2 = Tamanho('M')
    tamanho3 = Tamanho('G')

    self.__tamanhos.append(tamanho1)
    self.__tamanhos.append(tamanho2)
    self.__tamanhos.append(tamanho3)
  
  def imprime_cabecalho_tamanhos_cadastrados(self):
    self.__tela_tamanho.cabecalho_tamanhos_cadastrados()
