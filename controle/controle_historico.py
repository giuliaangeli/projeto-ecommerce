from itertools import count
from this import d
from limite.tela_historico import TelaHistorico
from entidade.historico import Historico
from entidade.usuario import Usuario
from entidade.cor import Cor
from entidade.tamanho import Tamanho
from entidade.categoria import Categoria
from entidade.produto import Produto

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

        for codigo in relatorio:
            produto = relatorio[codigo][0]
            quantidade = relatorio[codigo][1]
            self.__tela_historico.imprime_historico_generico(produto, quantidade)

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
        relatorio = {}
        lista_produtos = self.__controlador_sistema.controlador_produtos.retorna_lista_produtos()

        for produto in lista_produtos:
            vezes = self.conta_objetos(produto, lista_historico)
            relatorio[produto.codigo] = (produto, vezes)
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

    def listar_historico_por_pessoa(self):
        historico_pessoa = []
        opcao_pessoa = self.__tela_historico.filtro_cliente()

        if opcao_pessoa == 1:
            return self.__tela_historico

        elif opcao_pessoa == 2:
            usuario = self.valida_usuario()
            for venda in self.__historico:
                if venda.usuario == usuario:
                    historico_pessoa.append(venda)
            return historico_pessoa

        else:
            print('ATENÇÃO: Digite uma opção válida!')
            self.listar_historico_por_pessoa()

    def lista_somente_produtos(self, lista):
        lista_historico_produto = []

        for venda in lista:
            produto_vendido = venda.produto
            lista_historico_produto.append(produto_vendido)

        return lista_historico_produto
                
    def filtra_lista_por_cor(self, lista):
        lista_filtrada_cor = []
        opcao_cor = self.__tela_historico.filtro_cor()

        if opcao_cor == 1:
            return lista

        elif opcao_cor == 2:
            cor = self.valida_cor()
            for venda in lista:
                if venda.cor.nome == cor:
                    lista_filtrada_cor.append(venda)
            return lista_filtrada_cor
        else:
            print('ATENÇÃO: Digite uma opção válida!')
            self.filtra_lista_por_cor(lista)

    def filtrar_lista_por_tamanho(self, lista):
        lista_filtrada_tamanho = []
        opcao_tamanho = self.__tela_historico.filtro_tamanho()

        if opcao_tamanho == 1:
            return lista

        elif opcao_tamanho == 2:
            tamanho = self.valida_tamanho()
            for venda in lista:
                if venda.tamanho.descricao == tamanho:
                    lista_filtrada_tamanho.append(venda)
            return lista_filtrada_tamanho

        else:
            print('ATENÇÃO: Digite uma opção válida!')
            self.filtrar_lista_por_tamanho()

    def filtrar_lista_por_categoria(self, lista):
        lista_filtrada_categoria = []
        opcao_categoria = self.__tela_historico.filtro_categoria()

        if opcao_categoria == 1:
            return lista

        elif opcao_categoria == 2:
            categoria = self.valida_categoria()
            for venda in lista:
                if venda.categoria.tipo == categoria:
                    lista_filtrada_categoria.append(venda)
            return lista_filtrada_categoria

        else:
            print('ATENÇÃO: Digite uma opção válida!')
            self.filtrar_lista_por_categoria()

    def valida_usuario(self):
        usuario = self.__tela_historico.escolha_cliente()
        usuario = self.__controlador_sistema.controlador_pessoas.confere_usuario_cpf(usuario)

        if isinstance(usuario, Usuario):
            return usuario

        else:
            print('ATENÇÃO: o CPF digitado não está cadastrado em nosso sistema! Digite um CPF válido')
            self.valida_usuario()

    def valida_cor(self):
        cor = self.__tela_historico.escolha_cor()
        cor = self.__controlador_sistema.controlador_cores.confere_cor_nome(cor)

        if isinstance(cor, Cor):
            return cor

        else:
            print('ATENÇÃO: a cor digitada não está cadastrada em nosso sistema! Digite uma cor válida')
            self.valida_cor()

    def valida_tamanho(self):
        tamanho = self.__tela_historico.escolha_tamanho()
        tamanho = self.__controlador_sistema.controlador_tamanhos.confere_tamanho_descricao(tamanho)

        if isinstance(tamanho, Tamanho):
            return tamanho
        else:
            print('ATENÇÃO: o tamanho digitado não está cadastrado em nosso sistema! Digite um tamanho válido')
            self.valida_tamanho()
    
    def valida_categoria(self):
        categoria = self.__tela_historico.escolha_categoria()
        categoria = self.__controlador_sistema.controlador_categorias.confere_categoria_tipo(categoria)

        if isinstance(categoria, Categoria):
            return categoria

        else:
            print('ATENÇÃO: a categoria digitada não está cadastrada em nosso sistema! Digite uma categoria válida')
            self.valida_categoria()

    def listar_historico_personalizado(self):
        lista_pessoa = self.listar_historico_por_pessoa()
        lista_produtos = self.lista_somente_produtos(lista_pessoa)
        lista_cor = self.filtra_lista_por_cor(lista_produtos)
        lista_tamanho = self.filtrar_lista_por_tamanho(lista_cor)
        lista_categoria = self.filtrar_lista_por_categoria(lista_tamanho)
        relatorio_sem_nulos = []
        relatorio = self.relatorio_produtos_iguais(lista_categoria)
        for codigo in relatorio:
            if relatorio[codigo][1] != 0:
                relatorio_sem_nulos[codigo] = relatorio[codigo]

        self.listar_quantidade_produtos_historico(relatorio_sem_nulos)

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

    
    
    def instancia_historico(self):
        usuario1 = self.__controlador_sistema.controlador_pessoas.confere_usuario_cpf('09641787969')
        usuario2 = self.__controlador_sistema.controlador_pessoas.confere_usuario_cpf('99900011199')
        produto1 = self.__controlador_sistema.controlador_produtos.pega_produto_por_codigo(1)
        produto2 = self.__controlador_sistema.controlador_produtos.pega_produto_por_codigo(2)
        produto3 = self.__controlador_sistema.controlador_produtos.pega_produto_por_codigo(3)
        produto4 = self.__controlador_sistema.controlador_produtos.pega_produto_por_codigo(4)
        produto5 = self.__controlador_sistema.controlador_produtos.pega_produto_por_codigo(5)
        produto6 = self.__controlador_sistema.controlador_produtos.pega_produto_por_codigo(6)
    
        venda1 = Historico(usuario1, produto6)
        venda2 = Historico(usuario1, produto6)
        venda3 = Historico(usuario2, produto2)
        venda4 = Historico(usuario2, produto2)
        venda5 = Historico(usuario2, produto3)
        venda6 = Historico(usuario1, produto4)
        venda7 = Historico(usuario1, produto5)
        venda8 = Historico(usuario2, produto5)
        venda9 = Historico(usuario1, produto5)

        #Coloca venda na lista de Historicos
        self.__historico.append(venda1)
        self.__historico.append(venda2)
        self.__historico.append(venda3)
        self.__historico.append(venda4)
        self.__historico.append(venda5)
        self.__historico.append(venda6)
        self.__historico.append(venda7)
        self.__historico.append(venda8)
        self.__historico.append(venda8)
        self.__historico.append(venda9)


