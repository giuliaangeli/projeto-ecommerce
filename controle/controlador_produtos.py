from limite.tela_produto import TelaProduto
from entidade.produto import Produto

from random import randint


class ControladorProdutos():

  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__produtos = []
    self.__tela_produto = TelaProduto()

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
    dados_produto = self.__tela_produto.pega_dados_produto()

    cor = self.__controlador_sistema.controlador_cores.pega_produto_por_nome(dados_produto["nome"])
    tamanho = self.__controlador_sistema.controlador_tamanhos.pega_produto_por_codigo(dados_produto["codigo"])
    categoria = self.__controlador_sistema.controlador_categorias.pega_produto_por_tipo(dados_produto["tipo"])
    produto = Produto(cor, tamanho,categoria, randint(0, 100))
    self.__produtos.append(produto)

  #Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_produto(self):
    for e in self.__produtos:
      self.__tela_produto.mostra_produto({"codigo": e.codigo,"nome_cor": e.cor.nome,"codigo_cor": e.cor.codigo,"descricao_tamanho": e.tamanho.descricao,"codigo_tamanho": e.tamanho.codigo,"tipo_categoria": e.categoria.tipo,"codigo_categoria": e.categoria.codigo})

  def excluir_produto(self):
    self.lista_produto()
    codigo_produto = self.__tela_produto.seleciona_produto()
    produto = self.pega_produto_por_codigo(int(codigo_produto))

    if (produto is not None):
      self.__produtos.remove(produto)
      self.lista_produto()
    else:
      self.__tela_produto.mostra_mensagem("ATENCAO: Produto não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_produto, 2: self.lista_produto, 3: self.excluir_produto,0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_produto.tela_opcoes()]()
