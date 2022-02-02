from entidade.historico import *
from limite.tela_abstrata import *

class TelaHistorico():
    
    def adm_ou_usuario(self):
        
        cabecalho('SELECIONE UMA DAS OPÇÕES')
        opcoes = ['[1] Administrador','[2] Usuário']
        
        for item in opcoes:
            print(item)

        print(linha())

        opcao = leiaInt('Digite sua opção: ')
        return opcao

    def login(self):

        cabecalho('INSIRA SEUS DADOS')
        email = input('E-mail: ')
        senha = input('Senha: ')

        return {'email': email, 'senha': senha}

    def seleciona_usuario(self):
        cpf = input('Qual o CPF da pessoa que você deseja consultar o histórico?')
        
        return cpf

    def menu_historico_adm(self):
        
        opcoes = ['[1] Consultar Histórico','[2] Excluir Venda']
        
        for item in opcoes:
            print(item)

        print(linha())

        opcao = leiaInt('Sua opção: ')
        return opcao

    def mostra_historico(self):

        cabecalho('HISTÓRIO DE COMPRA')
        
        for compra in historico:
            print(compra)

        print(linha())

    