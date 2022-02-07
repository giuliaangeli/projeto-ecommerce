from itertools import count
from this import d
from limite.tela_historico import TelaHistorico
from entidade.historico import Historico

class ControladorHistorico():
    
    def __init__(self, controlador_sistema):
        self.__historico = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_historico = TelaHistorico()
    
    def incluir_historico(self):
        usuario = self.__controlador_sistema.controlador_pessoas.confere_usuario_cpf_historico()
        produto = self.__controlador_sistema.controlador_produtos.confere_produto_codigo()
        self.recebe_dados_venda(usuario, produto)

    def listar_quantidade_produtos_historico(self, relatorio):
        for venda in relatorio:
            self.__tela_historico.imprime_historico_generico({"codigo": venda.produto.codigo,"nome_cor": venda.produto.cor.nome,"descricao_tamanho": venda.produto.tamanho.descricao,"tipo_categoria": venda.produto.categoria.tipo, "quantidade": venda.vezes})

    def recebe_dados_venda(self, usuario, produto):
        venda = Historico(usuario, produto)
        self.__historico.append(venda)
        print('A venda foi adicionada ao histórico!')

    def confere_venda_historico(self):
        usuario = self.__controlador_sistema.controle_pessoas.confere_usuario_cpf_historico()
        produto = self.__controlador_sistema.controlador_produtos.confere_produto_codigo()
        venda_para_validar = Historico(usuario, produto)

        for venda in self.__historico:
            if venda == venda_para_validar:
                return venda
            else:
                print('ATENÇÃO: A venda informada não consta no histórico, tente novamente!')
                self.confere_venda_historico()

    def excluir_historico(self):
        venda_excluir = self.confere_venda_historico()
        self.__historico.remove(venda_excluir)

    def alterar_historico_produto(self):
        venda_alterar = self.confere_venda_historico()
        produto_alterado = self.__controlador_sistema.controlador_produtos.confere_produto_codigo()
        venda_alterar.produto = produto_alterado

    def listar_historico_usuario(self, usuario):
        historico_usuario = []
        for venda in self.__historico:
            if venda.usuario == usuario:
                historico_usuario.append(venda.produto)

        relatorio = self.relatorio_produtos_iguais(historico_usuario)
        self.listar_quantidade_produtos_historico(relatorio)

    def relatorio_produtos_iguais(self, lista_historico):
        relatorio = list
        lista_produtos = self.__controlador_sistema.controlador_produtos.retorna_lista_produtos()

        for produto in lista_produtos:
            vezes = self.conta_objetos(produto, lista_historico)
            relatorio.append(produto, vezes)
        return relatorio

    def conta_objetos(self, produto, lista_produtos_comprados):
        vezes = 0
        for compra in lista_produtos_comprados:
            if compra.cor.nome == produto.cor.nome and compra.tamanho.descricao == produto.tamanho.descricao and compra.categoria.tipo == produto.categoria.tipo:
                vezes =+ 1

        return vezes
        
    def listar_historico_simples(self):
        lista_historico_produto = []

        for venda in self.__historico:
            produto_vendido = venda.produto
            lista_historico_produto.append(produto_vendido)

        relatorio = self.relatorio_produtos_iguais(lista_historico_produto)
        self.listar_quantidade_produtos_historico(relatorio)

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
                lista_opcoes[opcao_escolhida](adm)

    def abrir_menu_historico_adm(self, adm):
         
        lista_opcoes = {1: self.abrir_menu_filtro_adm, 2: self.alterar_historico_produto, 3: self.incluir_historico, 4: self.excluir_historico, 5: self.voltar_menu_principal_adm, 6: self.__controlador_sistema.abre_tela_inicial}
        
        continua = True
        while continua:
            opcao_escolhida = self.__tela_historico.menu_principal_adm()
            if opcao_escolhida == 1 or opcao_escolhida == 5:
                lista_opcoes[opcao_escolhida](adm)
            else:
                lista_opcoes[opcao_escolhida]()

    