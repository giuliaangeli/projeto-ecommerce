from limite.tela_cor import TelaCor
from entidade.cor import Cor
from limite.ja_cadastrado import JaCadastrado
from limite.cadrasto import Cadastrado
from DAOs.cor_dao import CorDAO


class ControladorCores():
  # Fazer lançamento e tratamento de exceções, ao invés de apenas mostrar mensagem na tela.
  def __init__(self, controlador_sistema):
    #self.__cores = []
    self.__cores_DAO = CorDAO()
    self.__controlador_sistema = controlador_sistema
    self.__tela_cor = TelaCor()

  def confere_cor_nome(self, nome: str):
    for cor in self.__cores_DAO.get_all():
      if (cor.nome == nome):
        return cor
    return None

  def incluir_cor(self):
    dados_cor = self.__tela_cor.pega_dados_cor()
    dados_confere = self.confere_nome_cor(dados_cor['nome'])
    try:
      if dados_confere == None:
        cor = Cor(dados_cor["nome"])
        self.__cores_DAO.add(cor)
        raise Cadastrado
      else:
        raise JaCadastrado
    except JaCadastrado as j:
      self.__tela_cor.mostra_mensagem("Cor" + str(j))
    except Cadastrado as i:
      self.__tela_cor.mostra_mensagem("A cor foi" + str(i))

  def alterar_cor(self):
    self.__tela_cor.mostra_mensagem("ATENÇÃO: Digite o nome da cor que você deseja alterar")
    corAntiga = self.__tela_cor.seleciona_cor()
    corAntiga = corAntiga
    self.__tela_cor.mostra_mensagem("ATENÇÃO: Digite o nome da cor pelo qual você deseja substituir")
    corNova =self.__tela_cor.seleciona_cor()
    corNova = corNova
    verefica = False
    verefica1 = False
    for cor in self.__cores_DAO.get_all():
      if cor.nome == corAntiga:
        verefica = True
    for cor in self.__cores_DAO.get_all():
      if cor.nome == corNova:
        verefica1 = True
    if verefica == True and verefica1 != True:
      for cor in self.__cores_DAO.get_all():
        if cor.nome == corAntiga:
          cor.nome = corNova
          self.__tela_cor.mostra_mensagem("ATENÇÃO: Cor alterada com sucesso")
    else:
      self.__tela_cor.mostra_mensagem("ATENÇÃO: A cor que deseja alterar não se encontra na lista de cores")

  def lista_cor(self):
      self.__tela_cor.mostra_cor(self.__cores_DAO.get_all())

  def excluir_cor(self):
    nome_cor = self.__tela_cor.seleciona_cor()
    cor = self.confere_cor_nome(nome_cor)
    if(cor is not None):
          #self.__amigos.remove(amigo)
      self.__cores_DAO.remove(cor.nome)
      self.lista_cor()
    else:
      self.__tela_cor.mostra_mensagem("ATENCAO: Cor não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def confere_nome_cor(self,nome):
      for cor in self.__cores_DAO.get_all():
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

  '''def instancia_cor(self):
    vermelho = Cor('VERMELHO')
    laranja = Cor('LARANJA')
    rosa = Cor('ROSA')
    amarelo = Cor('AMARELO')
    verde = Cor('VERDE')
    
    self.__cores.append(vermelho)
    self.__cores.append(laranja)
    self.__cores.append(rosa)
    self.__cores.append(amarelo)
    self.__cores.append(verde)'''
  
  def imprime_cabecalho_cores_cadastradas(self):
    self.__tela_cor.cabecalho_cores_cadastradas()

  def incluir_cor(self, adm):
      dados_cor = self.__tela_cor.pega_dados_cor()
      dados_cor =  self.confere_output(adm, dados_cor)
      dados_confere = self.confere_nome_cor(dados_cor)

      try:
          if dados_confere == None:
              dados_cor = Cor(dados_cor)
              self.__cores.append(dados_cor)
              self.__tela_cor.mostra_mensagem("ATENÇÃO: COR foi adicionada com sucesso!")
          else:
              raise JaCadastrado
      except JaCadastrado as j:
          self.__tela_cor.mostra_mensagem("Essa COR " + str(j))

  def alterar_cor(self, adm):
      dados_nome = self.__tela_cor.alterar_dados_cor()
      dados_nome = self.confere_output(adm, dados_nome)
      nome_antigo = self.confere_cor_nome(dados_nome["nome_antigo"])

      if nome_antigo == None:
          self.__tela_cor.mostra_mensagem("ATENÇÃO: A COR que você deseja trocar não existe!")

      else:
          nome_novo = self.confere_cor_nome(dados_nome["nome_novo"])
          if nome_novo == None:
              nome_antigo.nome = dados_nome["nome_novo"]
              self.__tela_cor.mostra_mensagem("ATENÇÃO: A COR foi alterada com sucesso!")
          else:
              self.__tela_cor.mostra_mensagem("ATENÇÃO: A COR pela qual você deseja trocar já está cadastrada!")

  def lista_cor(self):
      self.__tela_cor.mostra_cor(self.__cores)

  def excluir_cor(self, adm):
      nome = self.__tela_cor.pega_dados_cor()

      for cor in self.__cores:
          if cor.nome == nome:
              self.__cores.remove(cor)
              return self.__tela_cor.mostra_mensagem("ATENÇÃO: Cor removida com sucesso")

      self.__tela_cor.mostra_mensagem("ATENÇÃO: Cor não cadastrada")

  def retornar(self):
      self.__controlador_sistema.abre_tela()

  def confere_nome_cor(self, nome):
      for cor in self.__cores:
          if (cor.nome == nome):
              return cor
      return None

  def retornar_menu__produto(self, adm):
      self.__controlador_sistema.controlador_produtos.menu_incluir_produto(
          adm)

  def abre_tela(self, adm):
      lista_opcoes = {1: self.incluir_cor, 2: self.alterar_cor, 3: self.lista_cor, 4: self.excluir_cor,
                      5: self.retornar_menu__produto, 6: self.__controlador_sistema.encerra_sistema}

      continua = True
      while continua:
          opcao_escolhida = self.__tela_cor.tela_opcoes()
          if opcao_escolhida == 3 or opcao_escolhida == 6:
              lista_opcoes[opcao_escolhida]()
          else:
              lista_opcoes[opcao_escolhida](adm)

  def instancia_cor(self):
      vermelho = Cor('VERMELHO')
      laranja = Cor('LARANJA')
      rosa = Cor('ROSA')
      amarelo = Cor('AMARELO')
      verde = Cor('VERDE')

      self.__cores.append(vermelho)
      self.__cores.append(laranja)
      self.__cores.append(rosa)
      self.__cores.append(amarelo)
      self.__cores.append(verde)

  def imprime_cabecalho_cores_cadastradas(self):
      self.__tela_cor.cabecalho_cores_cadastradas()
