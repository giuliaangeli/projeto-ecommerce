from limite.tela_sistema  import TelaSistema
from controle.controlador_cores import ControladorCores
from controle.controlador_tamanhos import ControladorTamanhos
from controle.controlador_categorias import ControladorCategorias
from controle.controlador_produtos import ControladorProdutos
from controle.controle_pessoas import ControladorPessoa

class ControladorSistema:

    def __init__(self):
        self.__controlador_cores = ControladorCores(self)
        self.__controlador_tamanhos = ControladorTamanhos(self)
        self.__controlador_categorias = ControladorCategorias(self)
        self.__controlador_produtos = ControladorProdutos(self)
        self.__controle_pessoas = ControladorPessoa(self)
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
        self.abre_tela_inicial()

    def cadastra_cores(self):
        self.__controlador_cores.abre_tela()

    def cadastra_tamanhos(self):
        self.__controlador_tamanhos.abre_tela()

    def cadastra_categorias(self):
        self.__controlador_categorias.abre_tela()

    def cadastra_produtos(self):
        self.__controlador_produtos.abre_tela()

    def cadastra_pessoas(self):
        self.__controle_pessoas.abre_tela()

    #def cadastra_carrinho(self):

    #def cadastra_historico(self):

    def encerra_sistema(self):
        exit(0)

    def abre_tela_inicial(self):
        self.__controle_pessoas.instancia_pessoas()

        #while True:
            
        opcao_escolhida = self.__tela_sistema.tela_inicial()

        #Pessoa escolhe fazer Login
        if opcao_escolhida == 1:
            opcao_escolhida = self.__tela_sistema.tela_login()

            #Pessoa escolhe fazer login como Administrador
            if opcao_escolhida == 1:
                adm = self.__controle_pessoas.confere_login(1)


                if adm is not None:
                    opcao_escolhida = self.__tela_sistema.tela_opcoes_adm()
                    print(opcao_escolhida)
                    
                    #opcao 1 - Pessoas
                    if opcao_escolhida == 1:
                        print("entrei na opção 1")
                        opcao_escolhida = self.__controle_pessoas.abre_tela_adm()
                    #opcao 2 - Produto
                    elif opcao_escolhida == 2:
                        opcao_escolhida = self.__controlador_produtos.abre_tela()
                    #opcao 3 - Historico
                    elif opcao_escolhida == 3:
                        print('Ainda em desenvolvimento')
                    #opcao 4 - Finalizar sessão
                    else:
                        self.encerra_sistema

            
            #Pessoa escolhe fazer login como usuário
            else:
                usuario = self.__controle_pessoas.confere_login(2)
                if usuario is not None:
                    opcao_escolhida = self.__tela_sistema.tela_opções_usuario()
        
        else: 
            self.__controle_pessoas.incluir_usuario()
        