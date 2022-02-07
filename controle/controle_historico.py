from this import d
from limite.tela_historico import TelaHistorico
from entidade.historico import Historico

class ControladorHistorico():
    
    def __init__(self, controlador_sistema):
        self.__historico = dict()
        self.__controlador_sistema = controlador_sistema
        self.__tela_historico = TelaHistorico()
    
    def incluir_historico(self):
        usuario = self.__controlador_sistema.controle_pessoas.confere_usuario_cpf_historico()
        produto = self.__controlador_sistema.controlador_produtos.confere_produto_codigo()
        self.recebe_dados_venda(usuario, produto)

    def recebe_dados_venda(self, usuario, produto):
        venda = Historico(usuario, produto)
        self.__historico.append(venda)
        print('A venda foi adicionada ao histórico!')

    def excluir_historico(self):
        # usuario = pass
        # produto = pass
        # for historico in self.__historico:
        #     if historico["Cliente"] == usuario and historico["Produto"] == produto:
        #         self.__historico.remove(historico)
        #         print("\nA venda foi removida do histórico com sucesso!\n")

        #     else:
        #         print("\nATENÇÃO: A venda desse produto para esse cliente não está no histórico\n")
        pass

    def alterar_historico_produto(self):
        # usuario = pass
        # produto = pass
        # produto_novo = passar
        # for historico in self.__historico:
        #     if historico["Cliente"] == usuario and historico["Produto"] == produto:
        #         historico["Produto"] == produto_novo
        #         print("\nHistorico alterado com sucesso!\n")

        #     else:
        #         print("\nATENÇÃO: A venda não foi substituida pois essa venda não consta no histórico\n")
        pass

    def listar_historico_usuario(self, usuario):
        # usuario
        # for historico in self.__historico:
        #     if historico["Cliente"] == usuario:
        #         produto = historico["Produto"]
        #         self.__tela_historico.imprime_historico_generico({"cor": produto.cor, "tamanho": produto.tamanho, "categoria": produto.categoria})
        pass
    def listar_historico_simples(self):
        pass

    def listar_historico_personalizado(self):
        pass

    def voltar_menu_principal_adm(self, adm):
        self.__controlador_sistema.controla_menu_principal_adm(adm)

    def abrir_menu_filtro_adm(self, adm):

        lista_opcoes = {1: self.listar_historico_simples, 2: self.listar_historico_personalizado, 3: self.abrir_menu_historico_adm, 4: self.__controlador_sistema.abre_tela_inicial}
        
        continua = True
        while continua:
            opcao_escolhida = self.__tela_historico.menu_opcao_filtro()
            if opcao_escolhida == 1 or opcao_escolhida == 2:
                lista_opcoes[opcao_escolhida]()
            else:
                lista_opcoes[opcao_escolhida]()

    def abrir_menu_historico_adm(self, adm):
         
        lista_opcoes = {1: self.abrir_menu_filtro_adm, 2: self.alterar_historico_produto, 3: self.incluir_historico, 4: self.excluir_historico, 5: self.voltar_menu_principal_adm, 6: self.__controlador_sistema.abre_tela_inicial}
        
        continua = True
        while continua:
            opcao_escolhida = self.__tela_historico.menu_principal_adm()
            if opcao_escolhida == 1 or opcao_escolhida == 5:
                lista_opcoes[opcao_escolhida](adm)
            else:
                lista_opcoes[opcao_escolhida]()

    