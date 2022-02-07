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
      print('Tamanho foi selecionada com sucesso!')
    else:
      print('Esse tamanho já está cadastrado')

  def alterar_tamanho(self):
    print("Digite a descricao do tamanho que você deseja alterar")
    tamanhoAntigo = input().upper()
    print("Digite a descricao do tamanho pelo qual você deseja substituir")
    tamanhoNovo = input().upper()
    verefica1 = False
    verefica = False
    for tamanho in self.__tamanhos:
      if tamanho.descricao == tamanhoAntigo:
        verefica = True
      if tamanho.descricao == tamanhoNovo:
        verefica1 = True
        print("O tamanho que você deseja alterar já se encontra na lista")
    if verefica == True and verefica1 != True:
      for tamanho in self.__tamanhos:
        if tamanho == tamanhoAntigo:
          tamanho.descricao = tamanhoNovo
          print("Tamanho alterada com sucesso")
    if verefica == False:
      print("O trabalho que deseja alterar não se encontra na lista de cores")

  # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_tamanho(self):
    for tamanho in self.__tamanhos:
      self.__tela_tamanho.mostra_tamanho({"descricao": tamanho.descricao})

  def excluir_tamanho(self):
    descricao = self.__tela_tamanho.seleciona_tamanho()
    for tamanho in self.__tamanhos:
      if tamanho.descricao == descricao:
        self.__tamanhos.remove(tamanho)
        print('Tamanho removido!')
      else:
        print("ATENÇÃO: esse tamanho não está cadastrado")
 
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
