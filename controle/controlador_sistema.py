from limite.tela_sistema import TelaSistema
from controle.controlador_cores import ControladorCores
from controle.controlador_tamanhos import ControladorTamanhos
from controle.controlador_categorias import ControladorCategorias
from controle.controlador_produtos import ControladorProdutos

class ControladorSistema:

    def __init__(self):
        self.__controlador_cores = ControladorCores(self)
        self.__controlador_tamanhos = ControladorTamanhos(self)
        self.__controlador_categorias = ControladorCategorias(self)
        self.__controlador_produtos = ControladorProdutos(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_cores(self):
        return self.__controlador_cores

    @property
    def controlador_tamanhos(self):
        return self.__controlador_tamanhos

    @property
    def controlador_categorias(self):
        return self.__controlador_categorias

    @property
    def controlador_produtos(self):
        return self.__controlador_produtos

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_cores(self):
        self.__controlador_cores.abre_tela()

    def cadastra_tamanhos(self):
        self.__controlador_tamanhos.abre_tela()

    def cadastra_categorias(self):
        self.__controlador_categorias.abre_tela()

    def cadastra_produtos(self):
        self.__controlador_produtos.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_cores, 2: self.cadastra_tamanhos, 3: self.cadastra_categorias,4: self.cadastra_produtos,0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
