from limite.tela_tamanho import TelaTamanho
from entidade.tamanho import Tamanho
from limite.ja_cadastrado import JaCadastrado

class ControladorTamanhos():
    # Fazer lançamento e tratamento de exceções, ao invés de apenas mostrar mensagem na tela.
    def __init__(self, controlador_sistema):
        self.__tamanhos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_tamanho = TelaTamanho()

    def confere_tamanho_descricao(self, descricao):
        for tamanho in self.__tamanhos:
            if (tamanho.descricao == descricao):
                return tamanho
        return None
    
    def confere_output(self, adm, output):
        if output == "Sair":
            self.__controlador_sistema.encerra_sistema()
        elif output == "Voltar":
            self.abre_tela(adm)
        else:
            return output

    def incluir_tamanho(self, adm):
        dados_tamanho = self.__tela_tamanho.pega_dados_tamanho()
        dados_tamanho = self.confere_output(adm, dados_tamanho)
        nova_tamanho = self.confere_tamanho_descricao(dados_tamanho)

        try:
            if nova_tamanho == None:
                tamanho = Tamanho(dados_tamanho)
                self.__tamanhos.append(tamanho)
                self.__tela_tamanho.mostra_mensagem("ATENÇÃO: TAMANHO foi adicionado com sucesso")
            else:
                raise JaCadastrado
        except JaCadastrado as j:
            self.__tela_tamanho.mostra_mensagem("Esse TAMANHO " + str(j))

    def alterar_tamanho(self, adm):
        dados_descricao = self.__tela_tamanho.alterar_dados_tamanho()
        dados_descricao = self.confere_output(adm, dados_descricao)
        descricao_antigo = self.confere_tamanho_descricao(dados_descricao["descricao_antigo"])

        if descricao_antigo == None:
            self.__tela_tamanho.mostra_mensagem("ATENÇÃO: O TAMANHO que você deseja trocar não existe!")

        else:
            descricao_novo = self.confere_tamanho_descricao(dados_descricao["descricao_novo"])
            if descricao_novo == None:
                descricao_antigo.descricao = dados_descricao["descricao_novo"]
                self.__tela_tamanho.mostra_mensagem("ATENÇÃO: O TAMANHO foi alterada com sucesso!")
            else:
                self.__tela_tamanho.mostra_mensagem("ATENÇÃO: O TAMANHO pela qual você deseja trocar já está cadastrada!")


    # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
    def lista_tamanho(self):
        
        self.__tela_tamanho.mostra_tamanho(self.__tamanhos)

    def excluir_tamanho(self, adm):
        descricao = self.__tela_tamanho.pega_dados_tamanho()
        
        for tamanho in self.__tamanhos:
            if tamanho.descricao == descricao:
                    self.__tamanhos.remove(tamanho)
                    return self.__tela_tamanho.mostra_mensagem("ATENÇÃO: Tamanho removido com sucesso")

        self.__tela_tamanho.mostra_mensagem("ATENÇÃO: Tamanho não cadastrado")

    def retornar_menu__produto(self, adm):
        self.__controlador_sistema.controlador_produtos.menu_incluir_produto(
            adm)

    def abre_tela(self, adm):
        lista_opcoes = {1: self.incluir_tamanho, 2: self.alterar_tamanho, 3: self.lista_tamanho,
                        4: self.excluir_tamanho, 5: self.retornar_menu__produto, 6: self.__controlador_sistema.encerra_sistema}

        continua = True
        while continua:
            opcao_escolhida = self.__tela_tamanho.tela_opcoes()
            if opcao_escolhida == 3 or opcao_escolhida == 6:
                lista_opcoes[opcao_escolhida]()
            else:
                lista_opcoes[opcao_escolhida](adm)

    def instancia_tamanho(self):
        tamanho1 = Tamanho('P')
        tamanho2 = Tamanho('M')
        tamanho3 = Tamanho('G')

        self.__tamanhos.append(tamanho1)
        self.__tamanhos.append(tamanho2)
        self.__tamanhos.append(tamanho3)

    def imprime_cabecalho_tamanhos_cadastrados(self):
        self.__tela_tamanho.cabecalho_tamanhos_cadastrados()
