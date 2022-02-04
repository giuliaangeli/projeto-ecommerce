from limite.tela_abstrata import *
class TelaSistema:
    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_inicial(self):
        cabecalho('BEM-VINDO(A)')
        opcoes = ['[1] Fazer Login','[2] Criar uma conta']
        
        for item in opcoes:
            print(item)

        print(linha())

        opcao = leiaInt('Digite sua opção: ')
        return opcao

    def tela_login(self):
        cabecalho('ESCOLHA UMA OPÇÃO')
        opcoes = ['[1] Login Administrador','[2] Login Cliente']
        
        for item in opcoes:
            print(item)

        print(linha())

        opcao = leiaInt('Digite sua opção: ')
        return opcao
        
    def tela_opcoes_adm(self):
        
        cabecalho('ESCOLHA UMA OPÇÃO')
        opcoes = ['[1] Pessoas','[2] Produtos','[3] Histórico', '[4] Finalizar Sessão']
        
        for item in opcoes:
            print(item)

        print(linha())

        opcao = leiaInt('Digite sua opção: ')


    def tela_opções_usuario(self):
        
        cabecalho('ESCOLHA UMA OPÇÃO')
        opcoes = ['[1] Ir as Compras','[2] Histórico de Compras','[3] Dados Pessoais', '[4] Finalizar Sessão']
        
        for item in opcoes:
            print(item)

        print(linha())

        opcao = leiaInt('Digite sua opção: ')