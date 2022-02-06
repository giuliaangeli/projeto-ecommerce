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
  def incluir_produto(self):

    self.__controlador_sistema.controlador_cores.lista_cor()
    self.__controlador_sistema.controlador_tamanhos.lista_tamanho()
    self.__controlador_sistema.controlador_categorias.lista_categoria()
    dados_produto = self.__tela_produtos.pega_dados_produto()

    cor = self.__controlador_sistema.controlador_cores.pega_cor_por_codigo(dados_produto["nome"])
    tamanho = self.__controlador_sistema.controlador_tamanhos.pega_tamanho_por_codigo(dados_produto["descricao"])
    categoria = self.__controlador_sistema.controlador_categorias.pega_categoria_por_codigo(dados_produto["tipo"])
    produto = Produto(cor, tamanho, categoria,randint(0,100))
    if produto in self.__produtos:
      print('Esse produto já está cadastrado')
    elif produto not in self.__produtos:
      self.__produtos.append(produto)
      print('Produto foi selecionada com sucesso!')


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

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_produto, 2: self.lista_produto, 3: self.excluir_produto,0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_produtos.tela_opcoes()]()
