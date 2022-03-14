from DAOs.categoria_dao import CategoriaDAO
from limite.tela_categoria import TelaCategoria
from entidade.categoria import Categoria
from limite.ja_cadastrado import JaCadastrado
from limite.cadrasto import Cadastrado

class ControladorCategorias():
  # Fazer lançamento e tratamento de exceções, ao invés de apenas mostrar mensagem na tela.
  def __init__(self, controlador_sistema):
    #self.__categorias = []
    self.__categorias_DAO = CategoriaDAO()
    self.__controlador_sistema = controlador_sistema
    self.__tela_categoria = TelaCategoria()

  def confere_categoria_tipo(self, tipo: str):
    for categoria in self.__categorias_DAO.get_all():
      if (categoria.tipo == tipo):
        return categoria
    return None
    
  def incluir_categoria(self):
    dados_categoria = self.__tela_categoria.pega_dados_categoria()
    nova_categoria = self.confere_categoria_tipo(dados_categoria["tipo"])

    try:
      if nova_categoria == None:
        categoria = Categoria(dados_categoria["tipo"])
        self.__categorias_DAO.add(categoria)
        raise Cadastrado
      else:
        
        raise JaCadastrado
    except JaCadastrado as j:
      self.__tela_categoria.mostra_mensagem("Cor não foi" + str(j))
    except Cadastrado as i:
      self.__tela_categoria.mostra_mensagem("A categoria foi" + str(i))

    def incluir_categoria(self, adm):
        dados_categoria = self.__tela_categoria.pega_dados_categoria()
        dados_categoria = self.confere_output(adm, dados_categoria)
        nova_categoria = self.confere_categoria_tipo(dados_categoria)

        try:
            if nova_categoria == None:
                categoria = Categoria(dados_categoria)
                self.__categorias.append(categoria)
                self.__tela_categoria.mostra_mensagem("ATENÇÃO: CATEGORIA adicionada com sucesso")
            else:
                raise JaCadastrado
        except JaCadastrado as j:
            self.__tela_categoria.mostra_mensagem("Essa CATEGORIA " + str(j))

    def alterar_categoria(self, adm):
        dados_tipo = self.__tela_categoria.alterar_dados_categoria()
        dados_tipo = self.confere_output(adm, dados_tipo)
        tipo_antigo = self.confere_categoria_tipo(dados_tipo["tipo_antigo"])

        if tipo_antigo == None:
            self.__tela_categoria.mostra_mensagem("ATENÇÃO: A CATEGORIA que você deseja trocar não existe!")

        else:
            tipo_novo = self.confere_categoria_tipo(dados_tipo["tipo_novo"])
            if tipo_novo == None:
                tipo_antigo.tipo = dados_tipo["tipo_novo"]
                self.__tela_categoria.mostra_mensagem("ATENÇÃO: A CATEGORIA foi alterada com sucesso!")
            else:
                self.__tela_categoria.mostra_mensagem("ATENÇÃO: A CATEGORIA pela qual você deseja trocar já está cadastrada!")

    self.__tela_categoria.mostra_categoria(self.__categorias_DAO.get_all())

  def excluir_categoria(self):
    self.lista_categoria()
    tipo_categoria = self.__tela_categoria.seleciona_categoria()
    categoria = self.confere_categoria_tipo(tipo_categoria)

  def excluir_categoria(self, adm):
      tipo = self.__tela_categoria.pega_dados_categoria()

      for categoria in self.__categorias:
          if categoria.tipo == tipo:
              self.__categorias.remove(categoria)
              return self.__tela_categoria.mostra_mensagem("ATENÇÃO: Categoria removida")
      
      self.__tela_categoria.mostra_mensagem("ATENÇÃO: Categoria não está cadastrada")

    
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

  '''  def instancia_categorias(self):
    categoria1 = Categoria('CALÇA')
    categoria2 = Categoria('CAMISETA')
    categoria3 = Categoria('MOLETON')
    categoria4 = Categoria('SHORT')

    self.__categorias_DAO.add(categoria1)
    self.__categorias_DAO.add(categoria2)
    self.__categorias_DAO.add(categoria3)
    self.__categorias_DAO.add(categoria4)'''

  @property
  def categorias(self):
    return self.__categorias_DAO.get_all()

  def imprime_cabecalho_categorias_cadastradas(self):
    self.__tela_categoria.cabecalho_categorias_cadastradas()
