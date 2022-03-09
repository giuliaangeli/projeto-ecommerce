#from pyparsing import sgl_quoted_string
from limite.tela_abstrata import *
import PySimpleGUI as sg
class TelaCor():
  def __init__(self):
    self.__window = None
    self.init_opcoes()
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    cabecalho('MENU CORES')
    opcao  = - 1
    while opcao == -1:
      self.init_opcoes()
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
      if values['6'] or button in (None,'Cancelar'):
        opcao = 6
      self.close()
    self.close()
    return opcao


  def init_opcoes(self):
   
    sg.ChangeLookAndFeel('DarkGrey3')
    layout = [
      [sg.Text('CORES ', font=("Helvica", 25))],
      [sg.Text('Escolha sua opção', font=("Helvica", 15))],
      [sg.Radio('Incluir cor', "RD1", key='1')],
      [sg.Radio('Alterar cor', "RD1", key='2')],
      [sg.Radio('Listar cor', "RD1", key='3')],
      [sg.Radio('Excluir cor', "RD1", key='4')],
      [sg.Radio('Voltar ao menu anterior', "RD1", key='5')],
      [sg.Radio('Sair', "RD1", key='6')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema de cores').Layout(layout)
  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_cor(self):
    print("DADOS COR ")
    sg.ChangeLookAndFeel('DarkGrey3')
    layout = [
      [sg.Text('DADOS COR ', font=("Helvica", 25))],
      [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema de livros').Layout(layout)

    button, values = self.open()
    nome = values['nome']

    self.close()
    return nome
    '''{"nome": nome}'''

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_cor(self, dados_cor):
    string_todas_cores = ""
    for cor in dados_cor:
      string_todas_cores = string_todas_cores + cor.nome +'\n'
    sg.Popup('LISTA DE COR ', string_todas_cores)

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_cor(self):
    sg.ChangeLookAndFeel('DarkGrey3')
    layout = [
      [sg.Text('SELECIONAR COR ', font=("Helvica", 25))],
      [sg.Text('Digite o nome da cor que deseja selecionar:', font=("Helvica", 15))],
      [sg.Text('nome:', size=(15, 1)), sg.InputText('', key='nome')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Seleciona cor').Layout(layout)

    button, values = self.open()
    nome = values['nome']
    self.close()
    return nome

  def mostra_mensagem(self, msg):
    sg.popup("", msg)

  def close(self):
    self.__window.Close()

  def open(self):
    button, values = self.__window.Read()
    return button, values
