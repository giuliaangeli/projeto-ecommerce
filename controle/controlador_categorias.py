from limite.tela_categoria import TelaCategoria
from entidade.categoria import Categoria

class ControladorCategorias():
  # Fazer lançamento e tratamento de exceções, ao invés de apenas mostrar mensagem na tela.
  def __init__(self, controlador_sistema):
    self.__categorias = []
    self.__controlador_sistema = controlador_sistema
    self.__tela_categoria = TelaCategoria()

  def pega_categoria_por_codigo(self, codigo: int):
    for categoria in self.__categorias:
      if(categoria.codigo == codigo):
        return categoria
    return None

  def incluir_categoria(self):
    dados_categoria = self.__tela_categoria.pega_dados_categoria()
    categoria = Categoria(dados_categoria["tipo"], dados_categoria["codigo"])
    self.__categorias.append(categoria)

  def alterar_categoria(self):
    self.lista_categoria()
    codigo_categoria = self.__tela_categoria.seleciona_categoria()
    categoria = self.pega_categoria_por_codigo(codigo_categoria)

    if(categoria is not None):
      novos_dados_categoria = self.__tela_categoria.pega_dados_categoria()
      categoria.tipo = novos_dados_categoria["tipo"]
      categoria.codigo = novos_dados_categoria["codigo"]
      self.lista_categoria()
    else:
      self.__tela_categoria.mostra_mensagem("ATENCAO: Categoria não existente")

  # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_categoria(self):
    for categoria in self.__categorias:
      self.__tela_categoria.mostra_categoria({"tipo": categoria.tipo, "codigo": categoria.codigo})

  def excluir_categoria(self):
    self.lista_categoria()
    codigo_categoria = self.__tela_categoria.seleciona_categoria()
    categoria = self.pega_categoria_por_codigo(codigo_categoria)

    if(categoria is not None):
      self.__categorias.remove(categoria)
      self.lista_categoria()
    else:
      self.__tela_categoria.mostra_mensagem("ATENCAO: Categoria não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_categoria, 2: self.alterar_categoria, 3: self.lista_categoria, 4: self.excluir_categoria, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_categoria.tela_opcoes()]()
