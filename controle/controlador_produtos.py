from entidade.categoria import Categoria
from entidade.tamanho import Tamanho
from limite.tela_abstrata import cabecalho
from limite.tela_produto import TelaProduto
from entidade.cor import Cor
from controle.controlador_cores import ControladorCores
from entidade.produto import Produto
from random import randint


# Fazer lançamento e tratamento de exceções, ao invés de apenas mostrar mensagem na tela.
class ControladorProdutos():

  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__produtos = []
    self.__tela_produtos = TelaProduto()

  def pega_produto_por_codigo(self, codigo: int):
    for produto in self.__produtos:
      if(produto.codigo == codigo):
        return produto
    return None

  #Sugestao: listar apenas os livros que não estão emprestados
  def incluir_produto(self, adm):

    cabecalho('CORES CADASTRADAS')
    self.__controlador_sistema.controlador_cores.lista_cor()
    cabecalho('TAMANHOS CADASTRADOS')
    self.__controlador_sistema.controlador_tamanhos.lista_tamanho()
    cabecalho('CATEGORIAS CADASTRADAS')
    self.__controlador_sistema.controlador_categorias.lista_categoria()
    dados_produto = self.__tela_produtos.pega_dados_produto()

    cor = self.valida_cor(dados_produto)
    tamanho = self.valida_tamanho(dados_produto)
    categoria = self.valida_categoria(dados_produto)
    codigo = len(self.__produtos) + 1
    novo_produto = Produto(cor, tamanho, categoria, codigo)

    for produto in self.__produtos:
      if produto == novo_produto:
        print('ATENÇÃO: o produto que você está tentando incluir já está na lista de produtos!')
      else:
        print('O produto foi adicionado a lista de produtos!')
        self.__produtos.append(novo_produto)

  def valida_cor(self, dados_produto):
    cor = self.__controlador_sistema.controlador_cores.confere_cor_nome(dados_produto["nome"])
    if isinstance(cor, Cor):
      return cor
    else:
      print('A cor digitada não está cadastrada na lista de cores, digite um cor válida!')
      self.valida_cor(dados_produto)


  def valida_tamanho(self, dados_produto):
    tamanho = self.__controlador_sistema.controlador_tamanhos.confere_tamanho_descricao(dados_produto["tamanho"])
    if isinstance(tamanho, Tamanho):
      return tamanho
    else:
      print('A cor digitada não está cadastrada na lista de tamanhos, digite um cor válida!')
      self.valida_tamanho(dados_produto)
  

  def valida_categoria(self, dados_produto):
    categoria = self.__controlador_sistema.controlador_categorias.confere_categoria_tipo(dados_produto["categoria"])
    if isinstance(categoria, Categoria):
      return categoria
    else:
      print('A cor digitada não está cadastrada na lista de categorias, digite um cor válida!')
      self.valida_categoria(dados_produto)
      
  #Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_produto(self):
    for e in self.__produtos:
      self.__tela_produtos.mostra_produto({"codigo": e.codigo,"nome_cor": e.cor.nome,"descricao_tamanho": e.tamanho.descricao,"tipo_categoria": e.categoria.tipo})

  def excluir_produto(self):
    self.lista_produto()
    codigo_produto = self.__tela_produtos.seleciona_produto()
    produto = self.pega_produto_por_codigo(int(codigo_produto))

    if (produto is not None) and (produto in self.__produtos):
      self.__produtos.remove(produto)
      self.lista_produto()
    else:
      self.__tela_produtos.mostra_mensagem("ATENCAO: Produto não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def confere_produto_cor(self, cor):
    for produto in self.__produtos:
      if (produto.cor == cor):
        return produto
    return None

  def confere_produto_tamanho(self, tamanho):
    for produto in self.__produtos:
      if (produto.tamanho == tamanho):
        return produto
    return None
  
  def confere_produto_categoria(self, categoria):
    for produto in self.__produtos:
      if (produto.categoria == categoria):
        return produto
    return None
  
  def alterar_produto(self):
    pass

  def retornar_tela_adm_principal(self, adm):
    self.__controlador_sistema.controla_menu_principal_adm(adm)

  def abre_tela_produtos_adm(self, adm):
    lista_opcoes = {1: self.menu_incluir_produto, 2: self.lista_produto, 3: self.alterar_produto, 4: self.excluir_produto, 5: self.retornar_tela_adm_principal, 6: self.__controlador_sistema.abre_tela_inicial}

    continua = True
    while continua:
      opcao_escolhida = self.__tela_produtos.tela_produtos_inicial_adm()
      if opcao_escolhida == 5 or opcao_escolhida == 1:
        lista_opcoes[opcao_escolhida](adm)
      else:
        lista_opcoes[opcao_escolhida]()
  
  def abre_menu_cor(self, adm):
    self.__controlador_sistema.controlador_cores.abre_tela(adm)

  def abre_menu_tamanho(self, adm):
    self.__controlador_sistema.controlador_tamanhos.abre_tela(adm)

  def abre_menu_categoria(self, adm):
    self.__controlador_sistema.controlador_categorias.abre_tela(adm)

  def retornar_tela_adm_produto(self, adm):
    self.abre_tela_produtos_adm(adm)

  def menu_incluir_produto(self, adm):

    lista_opcoes = {1: self.incluir_produto, 2: self.abre_menu_cor, 3: self.abre_menu_tamanho, 4: self.abre_menu_categoria, 5: self.retornar_tela_adm_produto, 6: self.__controlador_sistema.abre_tela_inicial}

    continua = True
    while continua:
      opcao_escolhida = self.__tela_produtos.tela_produtos__adm()
      if opcao_escolhida == 6:
        lista_opcoes[opcao_escolhida]()
      else:
        lista_opcoes[opcao_escolhida](adm)
        
  def usuario_compra_produto(self, usuario):
    pass

  def retorna_menu_principal_usuario(self, usuario):
    self.__controlador_sistema.controla_menu_principal_usuario(usuario)

  def abri_menu_usuario(self, usuario):
    lista_opcoes = {1: self.lista_produto, 2: self.usuario_compra_produto, 3: self.retorna_menu_principal_usuario, 4: self.__controlador_sistema.abre_tela_inicial}
    
    continua = True
    while continua:
      opcao_escolhida = self.__tela_produtos.tela_produto_usuario()
      if opcao_escolhida == 1 or opcao_escolhida == 4:
        lista_opcoes[opcao_escolhida]()
      else:
        lista_opcoes[opcao_escolhida](usuario)

  def instancia_produtos(self):
    cor1 = Cor('VERMELHO')
    cor2 = Cor('VERDE')
    cor3 = Cor('AMARELO')
    tamanho1 = Tamanho('P')
    tamanho2 = Tamanho('M')
    tamanho3 = Tamanho('G')
    categoria1 = Categoria('CAMISETA')
    categoria2 = Categoria('MOLETON')
    categoria3 = Categoria('SHORT')
    produto1 = Produto(cor1, tamanho1, categoria1, 1)
    produto2 = Produto(cor2, tamanho3, categoria2, 2)
    produto3 = Produto(cor3, tamanho1, categoria2, 3)
    produto4 = Produto(cor1, tamanho2, categoria3, 4)
    produto5 = Produto(cor2, tamanho2, categoria1, 5)
    produto6 = Produto(cor3, tamanho3, categoria3, 6)
    self.__produtos.append(produto1)
    self.__produtos.append(produto2)
    self.__produtos.append(produto3)
    self.__produtos.append(produto4)
    self.__produtos.append(produto5)
    self.__produtos.append(produto6)


