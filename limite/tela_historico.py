from entidade.historico import *
from limite.tela_abstrata import *

class TelaHistorico():

    def menu_principal_adm(self):
        
        cabecalho('SELECIONE UMA DAS OPÇÕES')
        opcoes = ['[1] Ver Histórico de Vendas','[2] Alterar Histórico de Vendas', '[3] Incluir uma Venda no Histórico', '[4] Excluir uma Venda do Histórico', '[5] Voltar ao Menu Anterior', '[6] Encerrar Sessão']
        
        for item in opcoes:
            print(item)

        print(linha())

        opcao = leiaInt('Digite sua opção: ')
        return opcao

    def menu_opcao_filtro(self):

        cabecalho('SELECIONE UMA DAS OPÇÕES')
        opcoes = ['[1] Ver Todas as Vendas','[2] Aplicar Filtro','[3] Voltar ao Menu Anterior', '[4] Encerrar Sessão']
        
        for item in opcoes:
            print(item)

        print(linha())

        opcao = leiaInt('Digite sua opção: ')
        return opcao

    def filtro_cor(self):
        cabecalho('SELECIONE UMA DAS OPÇÕES')
        opcoes = ['[1] Todas as Cores','[2] Escolher uma Cor']
        
        for item in opcoes:
            print(item)

        print(linha())

        opcao = leiaInt('Digite sua opção: ')
        return opcao

    def filtro_tamanho(self):
        cabecalho('SELECIONE UMA DAS OPÇÕES')
        opcoes = ['[1] Todos os Tamanhos','[2] Escolher um Tamanho']
        
        for item in opcoes:
            print(item)

        print(linha())

        opcao = leiaInt('Digite sua opção: ')
        return opcao

    def filtro_categoria(self):
        cabecalho('SELECIONE UMA DAS OPÇÕES')
        opcoes = ['[1] Todas as Categorias','[2] Escolher uma Categoria']
        
        for item in opcoes:
            print(item)

        print(linha())

        opcao = leiaInt('Digite sua opção: ')
        return opcao

    def filtro_cliente(self):

        cabecalho('SELECIONE UMA DAS OPÇÕES')
        opcoes = ['[1] Todos os Clientes','[2] Escolher um Cliente']
        
        for item in opcoes:
            print(item)

        print(linha())

        opcao = leiaInt('Digite sua opção: ')
        return opcao

    def escolha_cor(self):
        cabecalho('DIGITE UMA COR')
        cor = input().upper()
        cor = cor.strip()
        return cor

    def escolha_tamanho(self):
        cabecalho('DIGITE UM TAMANHO')
        tamanho = input().upper()
        tamanho = tamanho.strip()
        return tamanho

    def escolha_categoria(self):
        cabecalho('DIGITE A CATEGORIA')
        categoria = input().upper
        categoria = categoria.strip()
        return categoria
    
    def escolha_cliente(self):
        cabecalho('DIGITE O CPF DO CLIENTE')
        cpf = input().upper()
        cpf = cpf.strip()
        return cpf

    def imprime_historico_generico(self, produto, quantidade):
        print("PRODUTO: ", produto.categoria.tipo)
        print("COR: ", produto.cor.nome)
        print("TAMANHO: ", produto.tamanho.descricao)
        print("QUANTIDADE ", quantidade)
        print('\n')

    def imprime_historico_filtrado(self, dados_compra, quantidade, nome):
        print("CLIENTE: ", nome)
        print("PRODUTO: ", dados_compra["categoria"])
        print("COR: ", dados_compra["cor"])
        print("TAMANHO: ", dados_compra["tamanho"])
        print("QUANTIDADE VENDIDA: ", quantidade)
