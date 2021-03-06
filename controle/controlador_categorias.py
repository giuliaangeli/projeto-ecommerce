from limite.tela_categoria import TelaCategoria
from entidade.categoria import Categoria

class ControladorCategorias():
  # Fazer lançamento e tratamento de exceções, ao invés de apenas mostrar mensagem na tela.
  def __init__(self, controlador_sistema):
    self.__categorias = []
    self.__controlador_sistema = controlador_sistema
    self.__tela_categoria = TelaCategoria()

  def confere_categoria_tipo(self, tipo):
    for categoria in self.__categorias:
      if (categoria.tipo == tipo):
        return categoria
    return None
    
  def incluir_categoria(self):
    dados_categoria = self.__tela_categoria.pega_dados_categoria()
    nova_categoria = self.confere_categoria_tipo(dados_categoria["tipo"])

    if nova_categoria == None:
      categoria = Categoria(dados_categoria["tipo"])
      self.__categorias.append(categoria)
      print('Categoria foi selecionada com sucesso!')
    else:
      print('Essa categoria já está cadastrado')

  def alterar_categoria(self):
    print("Digite o nome da cor que você deseja alterar")
    corAntiga = input().upper()
    corAntiga = corAntiga.strip()
    print("Digite o nome da cor pelo qual você deseja substituir")
    corNova = input().upper()
    corNova = corNova.strip()
    verefica1 = False
    verefica = False
    for cor in self.__categorias:
      if cor.tipo == corAntiga:
        verefica = True
      if cor.tipo == corNova:
        verefica1 = False
        print("A cor que você deseja alterar já se encontra na lista")
    if verefica == True and verefica1 != True:
      for cor in self.__categorias:
        if cor.tipo == corAntiga:
          cor.tipo = corNova
          print("Cor alterada com sucesso")
    elif verefica == False:
      print("A cor que deseja alterar não se encontra na lista de cores")
        

  # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_categoria(self):
    for categoria in self.__categorias:
      self.__tela_categoria.mostra_categoria({"tipo": categoria.tipo})

  def excluir_categoria(self):
    tipo = self.__tela_categoria.seleciona_categoria()
    for categoria in self.__categorias:
      if categoria.tipo == tipo:
        self.__categorias.remove(categoria)
        print('Categoria removido!')
      else:
        print("ATENÇÃO: essa categoria não está cadastrado")
    
  def retornar_menu__produto(self, adm):
    self.__controlador_sistema.controlador_produtos.menu_incluir_produto(adm)

  def abre_tela(self, adm):
    lista_opcoes = {1: self.incluir_categoria, 2: self.alterar_categoria, 3: self.lista_categoria, 4: self.excluir_categoria, 5: self.retornar_menu__produto, 6: self.__controlador_sistema.abre_tela_inicial}
    
    continua = True
    while continua:
      opcao_escolhida = self.__tela_categoria.tela_opcoes()
      if opcao_escolhida == 5:
        lista_opcoes[opcao_escolhida](adm)
      else:
        lista_opcoes[opcao_escolhida]()

  def instancia_categorias(self):
    categoria1 = Categoria('CALÇA')
    categoria2 = Categoria('CAMISETA')
    categoria3 = Categoria('MOLETON')
    categoria4 = Categoria('SHORT')

    self.__categorias.append(categoria1)
    self.__categorias.append(categoria2)
    self.__categorias.append(categoria3)
    self.__categorias.append(categoria4)

  @property
  def categorias(self):
    return self.__categorias
