from limite.tela_tamanho import TelaTamanho
from entidade.tamanho import Tamanho

class ControladorTamanhos():
  # Fazer lançamento e tratamento de exceções, ao invés de apenas mostrar mensagem na tela.
  def __init__(self, controlador_sistema):
    self.__tamanhos = []
    self.__controlador_sistema = controlador_sistema
    self.__tela_tamanho = TelaTamanho()

  def pega_tamanho_por_codigo(self, descricao: str):#comentei
    for tamanho in self.__tamanhos:
      if(tamanho.descricao == descricao):#comentei
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
 
  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_tamanho, 2: self.alterar_tamanho, 3: self.lista_tamanho, 4: self.excluir_tamanho, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_tamanho.tela_opcoes()]()

  def confere_tamanho_descricao(self, descricao):
    for tamanho in self.__tamanhos:
      if (tamanho.descricao == descricao):
        return tamanho
    return None

  def instancia_tamanho(self):
    tamanho1 = Tamanho('P',1)
    tamanho2 = Tamanho('M',2)
    tamanho3 = Tamanho('G',3)

    self.__tamanhos.append(tamanho1)
    self.__tamanhos.append(tamanho2)
    self.__tamanhos.append(tamanho3)
