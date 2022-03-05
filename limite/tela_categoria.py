#from pyparsing import sgl_quoted_string
from limite.tela_abstrata import *
import PySimpleGUI as sg
class TelaCategoria():
  def __init__(self):
    self.__window = None
    self.init_opcoes()
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    cabecalho('MENU CATEGORIAS')
    self.init_opcoes()
    button, values = self.open()
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
    # cobre os casos de Retornar, fechar janela, ou clicar cancelar
    #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
    if values['6'] or button in (None, 'Cancelar'):
      opcao = 6
    self.close()
    return opcao


  def init_opcoes(self):
    # sg.theme_previewer()
    sg.ChangeLookAndFeel('DarkGrey3')
    layout = [
      [sg.Text('-------- CATEGORIAS ----------', font=("Helvica", 25))],
      [sg.Text('Escolha sua opção', font=("Helvica", 15))],
      [sg.Radio('Incluir categoria', "RD1", key='1')],
      [sg.Radio('Alterar categorias', "RD1", key='2')],
      [sg.Radio('Listar caategorias', "RD1", key='3')],
      [sg.Radio('Excluir categrias', "RD1", key='4')],
      [sg.Radio('Voltar ao menu anterior', "RD1", key='5')],
      [sg.Radio('Sair', "RD1", key='6')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema de categorias').Layout(layout)
  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_categoria(self):
    print("-------- DADOS CATEGORIAS ----------")
    sg.ChangeLookAndFeel('DarkGrey3')
    layout = [
      [sg.Text('-------- DADOS CATEGORIAS ----------', font=("Helvica", 25))],
      [sg.Text('Tipo:', size=(15, 1)), sg.InputText('', key='tipo')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema de categorias').Layout(layout)

    button, values = self.open()
    tipo = values

    self.close()
    return tipo
    #return {"tipo": tipo}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_categoria(self, dados_categoria):
    string_todos_categorias = dados_categoria
    #for dado in dados_categoria:
    #  string_todos_categorias = string_todos_categorias + "TIPO DA CATEGORIA: " + dado["tipo"] + '\n'

    sg.Popup('-------- LISTA DE CATEGORIA ----------', string_todos_categorias)

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_categoria(self):
    sg.ChangeLookAndFeel('DarkGrey3')
    layout = [
      [sg.Text('-------- SELECIONAR CATEGORIA ----------', font=("Helvica", 25))],
      [sg.Text('Digite o tipo da categoria que deseja selecionar:', font=("Helvica", 15))],
      [sg.Text('tipo:', size=(15, 1)), sg.InputText('', key='tipo')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Seleciona categoria').Layout(layout)

    button, values = self.open()
    tipo = values['tipo']
    self.close()
    return tipo

  def mostra_mensagem(self, msg):
    sg.popup("", msg)

  def close(self):
    self.__window.Close()

  def open(self):
    button, values = self.__window.Read()
    return button, values
