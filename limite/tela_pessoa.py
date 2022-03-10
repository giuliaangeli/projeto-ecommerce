from entidade.usuario import Usuario
from limite.tela_abstrata import *
#from pyparsing import sgl_quoted_string
import PySimpleGUI as sg


class TelaPessoa():
    def __init__(self):
        self.__window = None
        self.init_opcoes()
        self.init_opcoes1()
        self.init_opcoes2()
    def adm_ou_usuario(self):
        opcao  = - 1
        while opcao == -1:
          self.init_opcoes()
          button, values = self.__window.Read()
          if values['1']:
            opcao = 1
          if values['2']:
            opcao = 2
            # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
          if values['6'] or button in (None,'Cancelar'):
            opcao = 6
          self.close()
        self.close()
        return opcao
    def tela_pessoa_adm(self):
        cabecalho('Opções Administrador')
        opcao  = - 1
        while opcao == -1:
          self.init_opcoes1()
          button, values = self.__window.Read()
          if values['1']:
            opcao = 1
          if values['2']:
            opcao = 2
          if values['3']:
            opcao = 3
          if values['4']:
            opcao = 4
          if values['5']:
            opcao = 5
          if values['6']:
            opcao = 6
          if values['7']:
            opcao = 7
          if values['8']:
            opcao = 8
            # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
          if values['9'] or button in (None,'Cancelar'):
            opcao = 9
          self.close()
        self.close()
        return opcao
    def tela_pessoa_usuario(self):
        cabecalho('Opções Usuario')
        opcao  = - 1
        while opcao == -1:
          self.init_opcoes2()
          button, values = self.__window.Read()
          if values['1']:
            opcao = 1
          if values['2']:
            opcao = 2
          if values['3']:
            opcao = 3
          if values['4']:
            opcao = 4
            # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
          if values['5'] or button in (None,'Cancelar'):
            opcao = 5
          self.close()
        self.close()
        return opcao

    def init_opcoes(self):

        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('Menu Inicial ', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Administrador', "RD1", key='1')],
            [sg.Radio('Usuário', "RD1", key='2')],
            [sg.Radio('Encerrar Sessão', "RD1", key='6')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema E-commerce').Layout(layout)

    def init_opcoes1(self):

        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('Opções Administrador ', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Administrador', "RD1", key='1')],
            [sg.Radio('Excluir Administrador', "RD1", key='2')],
            [sg.Radio('Listar Administradores', "RD1", key='3')],
            [sg.Radio('Alterar meus Dados', "RD1", key='4')],
            [sg.Radio('Incluir Usuário', "RD1", key='5')],
            [sg.Radio('Excluir Usuário', "RD1", key='6')],
            [sg.Radio('Listar Usuário', "RD1", key='7')],
            [sg.Radio('Voltar ao Menu Anterior', "RD1", key='8')],
            [sg.Radio('Encerrar Sessão', "RD1", key='9')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema E-commerce').Layout(layout)

    def init_opcoes2(self):

        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('Dados ', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Consultar Dados', "RD1", key='1')],
            [sg.Radio('Alterar Dados', "RD1", key='2')],
            [sg.Radio('Excluir Conta', "RD1", key='3')],
            [sg.Radio('Voltar ao Menu Anterior', "RD1", key='4')],
            [sg.Radio('Encerrar Sessão', "RD1", key='5')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema E-commerce').Layout(layout)
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado

    def pega_dados_usuario(self):
        print("DADOS ")
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('DADOS  ', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text('Telefone:', size=(15, 1)),
             sg.InputText('', key='telefone')],
            [sg.Text('Endereço:', size=(15, 1)),
             sg.InputText('', key='endereco')],
            [sg.Text('E-mail:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Text('Senha:', size=(15, 1)), sg.InputText('', key='senha')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema E-commerce').Layout(layout)
        button, values = self.open()
        nome = values['nome']
        cpf = values['cpf']
        telefone = values['telefone']
        endereco = values['endereco']
        email = values['email']
        senha = values['senha']

        self.close()
        return {"nome": nome, 'cpf': cpf, 'telefone': telefone, 'endereco': endereco, 'email': email, 'senha': senha}

    def pega_dado_adm(self):
        print("DADOS ")
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('DADOS ', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text('Telefone:', size=(15, 1)),
             sg.InputText('', key='telefone')],
            [sg.Text('Endereço:', size=(15, 1)),
             sg.InputText('', key='endereco')],
            [sg.Text('E-mail:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Text('Senha:', size=(15, 1)), sg.InputText('', key='senha')],
            [sg.Text('Salario:', size=(15, 1)),
             sg.InputText('', key='salario')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema E-commerce').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        cpf = values['cpf']
        telefone = values['telefone']
        endereco = values['endereco']
        email = values['email']
        senha = values['senha']
        salario = values['salario']

        self.close()
        return {"nome": nome, 'cpf': cpf, 'telefone': telefone, 'endereco': endereco, 'email': email, 'senha': senha, 'salario': salario}

    def pega_dados_login(self):
        print("DADOS  ")
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('DADOS  ', font=("Helvica", 25))],
            [sg.Text('E-mail:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Text('Senha:', size=(15, 1)), sg.InputText('', key='senha')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema E-commerce').Layout(layout)

        button, values = self.open()
        email = values['email']
        senha = values['senha']

        self.close()
        return {'email': email, 'senha': senha}

    def pega_cpf(self):
        print("DADOS ")
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('DADOS  ', font=("Helvica", 25))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema E-commerce').Layout(layout)

        button, values = self.open()
        cpf = values['cpf']

        self.close()
        return cpf

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostra_adm(self, dados_adms):
        string_dados_adms = ""
        for adm in dados_adms:
            string_dados_adms = string_dados_adms + 'NOME: ' + adm.nome + '\n'
            string_dados_adms = string_dados_adms + 'CPF: ' + adm.cpf + '\n'
            string_dados_adms = string_dados_adms + 'TELEFONE: ' + adm.telefone + '\n'
            string_dados_adms = string_dados_adms + 'ENDEREÇO: ' + adm.endereco + '\n'
            string_dados_adms = string_dados_adms + 'EMAIL: ' + adm.email + '\n\n'
        sg.Popup('ADM CADASTRADOS', string_dados_adms)

    def mostra_usuario(self, tipo, dados_usuario):

        string_dados_usuário = ""
        if tipo == 1:
            for usuario in dados_usuario:
                string_dados_usuário = string_dados_usuário + 'NOME: ' + usuario.nome + '\n'
                string_dados_usuário = string_dados_usuário + 'CPF: ' + usuario.cpf + '\n'
                string_dados_usuário = string_dados_usuário + 'TELEFONE: ' + usuario.telefone + '\n'
                string_dados_usuário = string_dados_usuário + 'ENDEREÇO: ' + usuario.endereco + '\n'
                string_dados_usuário = string_dados_usuário + 'EMAIL: ' + usuario.email + '\n\n'
            sg.Popup('USUÁRIOS CADASTRADOS', string_dados_usuário)

        else:
            for usuario in dados_usuario:
                string_dados_usuário = string_dados_usuário + 'NOME: ' + usuario.nome + '\n'
                string_dados_usuário = string_dados_usuário + 'CPF: ' + usuario.cpf + '\n'
                string_dados_usuário = string_dados_usuário + 'TELEFONE: ' + usuario.telefone + '\n'
                string_dados_usuário = string_dados_usuário + 'ENDEREÇO: ' + usuario.endereco + '\n'
                string_dados_usuário = string_dados_usuário + 'EMAIL: ' + usuario.email + '\n'
                string_dados_usuário = string_dados_usuário + 'SENHA: ' + usuario.senha + '\n\n'
            sg.Popup('SEUS DADOS', string_dados_usuário)

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
