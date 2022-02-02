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