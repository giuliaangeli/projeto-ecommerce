from limite.tela_abstrata import *
class TelaSistema:
    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_inicial(self):
        cabecalho('BEM-VINDO(A)')
        opcoes = ['[1] Fazer Login','[2] Criar uma conta']
     
        for item in opcoes:
            print(item)

        print(linha())

        while True:
            try:
                opcao = leiaInt('Digite sua opção: ')
                if ( opcao != 1 and opcao != 2):
                    raise ValueError
                return opcao        
            except ValueError:
                print("O valor digitado deve ser um inteiro de 1 a 2")


    def tela_login(self):
        cabecalho('ESCOLHA UMA OPÇÃO')
        opcoes = ['[1] Login Administrador','[2] Login Cliente']
        
        for item in opcoes:
            print(item)

        print(linha())

        while True:
            try:
                opcao = leiaInt('Digite sua opção: ')
                if ( opcao != 1 and opcao != 2):
                    raise ValueError
                return opcao        
            except ValueError:
                print("O valor digitado deve ser um inteiro de 1 a 2")

    def falha(self):

        print('Escolha uma das opções abaixo')
        opcoes = ['[1] Tentar novamente','[2] Voltar ao menu anterior']
        
        for item in opcoes:
            print(item)

        print(linha())

        while True:
            try:
                opcao = leiaInt('Digite sua opção: ')
                if ( opcao != 1 and opcao != 2):
                    raise ValueError
                return opcao        
            except ValueError:
                print("O valor digitado deve ser um inteiro de 1 a 2")
        
    def tela_opcoes_adm(self):
        
        cabecalho('ESCOLHA UMA OPÇÃO')
        opcoes = ['[1] Pessoas','[2] Produtos','[3] Histórico', '[4] Finalizar Sessão']
        
        for item in opcoes:
            print(item)

        print(linha())

        while True:
            try:
                opcao = leiaInt('Digite sua opção: ')
                if ( opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4):
                    raise ValueError
                return opcao        
            except ValueError:
                print("O valor digitado deve ser um inteiro de 1 a 4")


    def tela_opcoes_usuario(self):
        
        cabecalho('ESCOLHA UMA OPÇÃO')
        opcoes = ['[1] Ir as Compras','[2] Histórico de Compras','[3] Dados Pessoais', '[4] Finalizar Sessão']
        
        for item in opcoes:
            print(item)

        print(linha())

        while True:
            try:
                opcao = leiaInt('Digite sua opção: ')
                if ( opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4):
                    raise ValueError
                return opcao        
            except ValueError:
                print("O valor digitado deve ser um inteiro de 1 a 4")
