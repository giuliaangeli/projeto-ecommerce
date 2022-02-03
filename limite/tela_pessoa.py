from limite.tela_abstrata import *
from controle.controle_pessoas import ControladorPessoa

class TelaPessoa():

    def adm_ou_usuario(self):
        
        cabecalho('CADASTRO DE...')
        opcoes = ['[1] Administrador','[2] Usuário']
        
        for item in opcoes:
            print(item)

        print(linha())

        opcao = leiaInt('Digite sua opção: ')
        return opcao

    def tela_opcoes(self):

        opcoes = ['[1] Incluir','[2] Alterar', '[3] Excluir', '[4] Listar', '[0] Retornar']
        
        for item in opcoes:
            print(item)

        print(linha())

        opcao = leiaInt('Sua opção: ')
        return opcao

    def pega_dados_usuario(self):

        cabecalho('Insira os dados abaixo')

        nome = input("Nome: ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")
        endereco = input("Endereço: ")
        email = input("E-mail: ")
        senha = input("Senha: ")

        return {'nome': nome, 'cpf': cpf, 'telefone': telefone, 'endereco': endereco,  'email': email, 'senha':  senha}

    def pega_dado_adm(self):

        cabecalho('Insira os dados abaixo')

        nome = input("Nome: ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")
        endereco = input("Endereço: ")
        email = input("E-mail: ")
        senha = input("Senha: ")
        salario = input("Salário: ")

        return {'nome': nome, 'cpf': cpf, 'telefone': telefone, 'endereco': endereco,  'email': email, 'senha':  senha, 'salario': salario}

    def mostra_adm(self, dados_adm):
        print("NOME: ", dados_adm["nome"])
        print("CPF: ", dados_adm["cpf"])
        print("TELEFONE: ", dados_adm["telefone"])
        print("ENDEREÇO: ", dados_adm["endereco"]) 
        print("E-MAIL: ", dados_adm["email"])
        print("SENHA: ", dados_adm["senha"])
        print("SALÁRIO: ", dados_adm["salario"])

    def mostra_usuario(self, dados_usuario):
        print("NOME: ", dados_usuario["nome"])
        print("CPF: ", dados_usuario["cpf"])
        print("TELEFONE: ", dados_usuario["telefone"])
        print("ENDEREÇO: ", dados_usuario["endereco"]) 
        print("E-MAIL: ", dados_usuario["email"])
        print("SENHA: ", dados_usuario["senha"])
    
    def seleciona_pessoa(self, tipo_pessoa):
        email = input("Digite seu e-mail: ")
        senha = input("Digite a sua senha: ")
        return {'email': email, 'senha': senha}

    

        

