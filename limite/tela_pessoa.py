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

    def tela_pessoa_adm(self):
        
        cabecalho('ESCOLHA UMA OPÇÃO')
        opcoes = ['[1] Incluir Administrador','[2] Listar Administradores','[3] Alterar Administrador', '[4] Excluir Administrador', '[5] Incluir Usuário','[6] Listar Usuários','[7] Excluir Usuário', '[8] Voltar ao Menu Anterior']
        
        for item in opcoes:
            print(item)

        print(linha())

        opcao = leiaInt('Digite sua opção: ')

        return opcao

    def tela_pessoa_usuario(self):

        cabecalho('ESCOLHA UMA OPÇÃO')
        opcoes = ['[1] Consultar Dados','[2] Alterar Dados', '[3] Excluir Conta']
        
        for item in opcoes:
            print(item)

        print(linha())

        opcao = leiaInt('Digite sua opção: ')

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
        print("\n")

    def mostra_usuario(self, dados_usuario):
        print("NOME: ", dados_usuario["nome"])
        print("CPF: ", dados_usuario["cpf"])
        print("TELEFONE: ", dados_usuario["telefone"])
        print("ENDEREÇO: ", dados_usuario["endereco"]) 
        print("E-MAIL: ", dados_usuario["email"])
        print("SENHA: ", dados_usuario["senha"])
        print("\n")
    
    # tirei o tipo de pessoa (adm ou usuário) pq não vai precisar
    def pega_dados_login(self):
        email = input("Digite seu e-mail: ")
        senha = input("Digite a sua senha: ")
        return {'email': email, 'senha': senha}

    def pega_cpf(self):
        cpf = input()
        return cpf
    

        

