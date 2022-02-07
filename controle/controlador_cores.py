from limite.tela_cor import TelaCor
from entidade.cor import Cor

class ControladorCores():
  # Fazer lançamento e tratamento de exceções, ao invés de apenas mostrar mensagem na tela.
  def __init__(self, controlador_sistema):
    self.__cores = []
    self.__controlador_sistema = controlador_sistema
    self.__tela_cor = TelaCor()

  def confere_cor_nome(self, nome):
    for cor in self.__cores:
      if (cor.nome == nome):
        return cor
    return None

  def incluir_cor(self):
    dados_cor = self.__tela_cor.pega_dados_cor()
    dados_confere = self.confere_nome_cor(dados_cor)
    if dados_confere == None:
      dados_cor = Cor(dados_cor)
      self.__cores.append(dados_cor)
      print('COR foi adicionada com sucesso!')
    else:
      print('Essa COR já está cadastrada')

  def alterar_cor(self):
    print("Digite o nome da cor que você deseja alterar")
    corAntiga = input().upper()
    print("Digite o nome da cor pelo qual você deseja substituir")
    corNova = input().upper()
    verefica1 = False
    verefica = False
    for cor in self.__cores:
      if cor.nome == corAntiga:
        verefica = True
      if cor.nome == corNova:
        verefica1 = False
        print("A cor que você deseja alterar já se encontra na lista")
    if verefica == True and verefica1 != True:
      for cor in self.__cores:
        if cor.nome == corAntiga:
          cor.nome = corNova
          print("Cor alterada com sucesso")
    elif verefica == False:
      print("A cor que deseja alterar não se encontra na lista de cores")   

  def lista_cor(self):
    for cor in self.__cores:
      self.__tela_cor.mostra_cor({"nome": cor.nome})

  def excluir_cor(self):
    nome = self.__tela_cor.seleciona_cor()
    for cor in self.__cores:
      if cor.nome == nome:
        self.__cores.remove(cor)
        print('COR removido!')
      else:
        print("ATENÇÃO: essa cor não está cadastrado")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def confere_nome_cor(self,nome):
      for cor in self.__cores:
        if (cor.nome  == nome):
          return cor
      return None
  
  def retornar_menu__produto(self, adm):
    self.__controlador_sistema.controlador_produtos.menu_incluir_produto(adm)

  def abre_tela(self, adm):
    lista_opcoes = {1: self.incluir_cor, 2: self.alterar_cor, 3: self.lista_cor, 4: self.excluir_cor, 5: self.retornar_menu__produto, 6: self.__controlador_sistema.abre_tela_inicial}

    continua = True
    while continua:
      opcao_escolhida = self.__tela_cor.tela_opcoes()
      if opcao_escolhida == 5:
        lista_opcoes[opcao_escolhida](adm)
      else:
        lista_opcoes[opcao_escolhida]()

  def instancia_cor(self):
    vermelho = Cor('VERMELHO')
    laranja = Cor('LARANJA')
    rosa = Cor('ROSA')
    amarelo = Cor('AMARELO ')
    verde = Cor('VERDE ')
    
    self.__cores.append(vermelho)
    self.__cores.append(laranja)
    self.__cores.append(rosa)
    self.__cores.append(amarelo)
    self.__cores.append(verde)

      
