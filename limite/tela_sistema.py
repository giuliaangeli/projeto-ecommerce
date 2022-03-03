import PySimpleGUI as sg

class TelaSistema:
    def __init__(self):
        self.__window = None
        self.init_components()
        self.init_components1()
        self.init_components2()
        self.init_components3()
        self.init_components4()

    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
# precisa chamar self.init_components() aqui para o caso de chamar essa janela uma 2a vez. Não é possível reusar layouts de janelas depois de fechadas.
    def tela_inicial(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def tela_login(self):
        self.init_components1()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao
    def falha(self):
        self.init_components2()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao
    def tela_opcoes_adm(self):
        self.init_components3()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if values['4'] or button in (None,'Cancelar'):
            opcao = 4
        self.close()
        return opcao

    def tela_opcoes_usuario(self):
        self.init_components4()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if values['4'] or button in (None,'Cancelar'):
            opcao = 4
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem vindo ao sistema E-commerce!', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Fazer login',"RD1", key='1')],
            [sg.Radio('Criar uma conta',"RD1", key='2')],
            [sg.Radio('Finalizar sistema',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema E-commerce').Layout(layout)
    def init_components1(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem vindo ao sistema E-commerce!', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Login Administrador',"RD1", key='1')],
            [sg.Radio('Login Cliente',"RD1", key='2')],
            [sg.Radio('Finalizar sistema',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema E-commerce').Layout(layout)

    def init_components2(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem vindo ao sistema E-commerce!', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Tentar novamente',"RD1", key='1')],
            [sg.Radio('Vltar ao menu anterior',"RD1", key='2')],
            [sg.Radio('Finalizar sistema',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema E-commerce').Layout(layout)

    def init_components3(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem vindo ao sistema E-commerce!', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Pessoas',"RD1", key='1')],
            [sg.Radio('Produtos',"RD1", key='2')],
            [sg.Radio('Histórico',"RD1", key='3')],
            [sg.Radio('Finalizar sistema',"RD1", key='4')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema E-commerce').Layout(layout)

    def init_components4(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem vindo ao sistema E-commerce!', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Ir as Compras',"RD1", key='1')],
            [sg.Radio('Histórico de Compras',"RD1", key='2')],
            [sg.Radio('Dados Pessoais',"RD1", key='3')],
            [sg.Radio('Finalizar sistema',"RD1", key='4')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema E-commerce').Layout(layout)
