from this import d
from limite.tela_historico import TelaHistorico
from entidade.historico import Historico

class ControladorHistorico():
    
    def __init__(self, controlador_sistema):
        self.__historico = dict()
        self.__controlador_sistema = controlador_sistema
        self.__tela_historico = TelaHistorico()
    
    def incluir_historico(self, codigo, usuario):
        produto = self.__controlador_sistema.controlador_produtos.selecionar_produto(codigo)
        self.__historico["Cliente"] = usuario
        self.__historico["Produto"] = produto

    def excluir_historico(self, usuario, produto):
        for historico in self.__historico:
            if historico["Cliente"] == usuario and historico["Produto"] == produto:
                self.__historico.remove(historico)
                print("\nA venda foi removida do histórico com sucesso!\n")

            else:
                print("\nATENÇÃO: A venda desse produto para esse cliente não está no histórico\n")

    def alterar_historico_produto(self, usuario, produto, produto_novo):
        for historico in self.__historico:
            if historico["Cliente"] == usuario and historico["Produto"] == produto:
                historico["Produto"] == produto_novo
                print("\nHistorico alterado com sucesso!\n")

            else:
                print("\nATENÇÃO: A venda não foi substituida pois essa venda não consta no histórico\n")

    def listar_historico_usuario(self, usuario):
        for historico in self.__historico:
            if historico["Cliente"] == usuario:
                produto = historico["Produto"]
                self.__tela_historico.imprime_historico_generico({"cor": produto.cor, "tamanho": produto.tamanho, "categoria": produto.categoria})

