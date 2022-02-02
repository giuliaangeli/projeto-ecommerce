from limite.tela_abstrata import *

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

        return {'salario': salario, 'nome': nome, 'cpf': cpf, 'telefone': telefone, 'endereco': endereco,  'email': email, 'senha':  senha}
        
    def mostra_pessoa(self, dados_pessoa):
        print("NOME: ", dados["nome"])
        print("CPF: ", dados["cpf"])
        print("TELEFONE: ", dados["telefone"])
        print("ENDEREÇO: ", dados["endereco"]) 
        print("E-MAIL: ", dados["email"])
        print("SENHA: ", dados["senha"])

    def seleciona_pessoa(self):
        cpf = input("Digite seu CPF: ")
        senha = input("Digite a sua senha: ")

    

        

