#from pyparsing import sgl_quoted_string
from limite.tela_abstrata import *
import PySimpleGUI as sg
class TelaTamanho():
  def __init__(self):
    self.__window = None
    self.init_opcoes()
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    cabecalho('MENU TAMANHO')
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
   
    sg.ChangeLookAndFeel('DarkGrey3')
    layout = [
      [sg.Text('TAMANHOS ', font=("Helvica", 25))],
      [sg.Text('Escolha sua opção', font=("Helvica", 15))],
      [sg.Radio('Incluir tamanhos', "RD1", key='1')],
      [sg.Radio('Alterar tamanhos', "RD1", key='2')],
      [sg.Radio('Listar tamanhos', "RD1", key='3')],
      [sg.Radio('Excluir tamanhos', "RD1", key='4')],
      [sg.Radio('Voltar ao menu anterior', "RD1", key='5')],
      [sg.Radio('Sair', "RD1", key='6')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema de tamanhos').Layout(layout)
  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_tamanho(self):
    print("DADOS TAMANHO ")
    sg.ChangeLookAndFeel('DarkGrey3')
    layout = [
      [sg.Text('DADOS TAMANHOS ', font=("Helvica", 25))],
      [sg.Text('Descricao:', size=(15, 1)), sg.InputText('', key='descricao')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema de tamanhos').Layout(layout)

    button, values = self.open()
    descricao = values

    self.close()
    return descricao
    #return {"descricao": descricao}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_tamanho(self, dados_tamanho):
    string_todos_tamanhos = ""
    for tamanho in dados_tamanho:
      string_todos_tamanhos = string_todos_tamanhos + tamanho.descricao +'\n'
    sg.Popup('LISTA DE TAMANHOS ', string_todos_tamanhos)

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_tamanho(self):
    sg.ChangeLookAndFeel('DarkGrey3')
    layout = [
      [sg.Text('SELECIONAR TAMANHO ', font=("Helvica", 25))],
      [sg.Text('Digite a descrição do tamanho que deseja selecionar:', font=("Helvica", 15))],
      [sg.Text('descricao:', size=(15, 1)), sg.InputText('', key='descricao')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Seleciona tamanho').Layout(layout)

    button, values = self.open()
    descricao = values['descricao']
    self.close()
    return descricao

  def mostra_mensagem(self, msg):
    sg.popup("", msg)

  def close(self):
    self.__window.Close()

  def open(self):
    button, values = self.__window.Read()
    return button, values
