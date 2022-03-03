from pyparsing import sgl_quoted_string
from limite.tela_abstrata import *
import PySimpleGUI as sg
from entidade.historico import *
class TelaHistorico():
  def __init__(self):
    self.__window = None
    self.init_opcoes()
    self.init_opcoes1()
    self.init_opcoes2()
    self.init_opcoes3()
    self.init_opcoes4()
    self.init_opcoes5()
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def menu_principal_adm(self):
    cabecalho('MENU HISTORICO')
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

  def menu_opcao_filtro(self):
    cabecalho('MENU HISTORICO')
    self.init_opcoes1()
    button, values = self.open()
    if values['1']:
      opcao = 1
    if values['2']:
      opcao = 2
    if values['3']:
      opcao = 3
    # cobre os casos de Retornar, fechar janela, ou clicar cancelar
    #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
    if values['4'] or button in (None, 'Cancelar'):
      opcao = 4
    self.close()
    return opcao


  def filtro_cor(self):
    #opcoes = ['[1] Ver Produtos Disponíveis','[2] Comprar um Produto Agora','[3] Voltar ao Menu Anterior', '[4] Finalizar Sessão']
    cabecalho('MENU HISTORICO')
    self.init_opcoes2()
    button, values = self.open()
    if values['1']:
      opcao = 1
    if values['2']:
      opcao = 2
    # cobre os casos de Retornar, fechar janela, ou clicar cancelar
    #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
    if values['0'] or button in (None, 'Cancelar'):
      opcao = 0
    self.close()
    return opcao
  def filtro_tamanho(self):
    #opcoes = ['[1] Ver Produtos Disponíveis','[2] Comprar um Produto Agora','[3] Voltar ao Menu Anterior', '[4] Finalizar Sessão']
    cabecalho('MENU HISTORICO')
    self.init_opcoes3()
    button, values = self.open()
    if values['1']:
      opcao = 1
    if values['2']:
      opcao = 2
    # cobre os casos de Retornar, fechar janela, ou clicar cancelar
    #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
    if values['0'] or button in (None, 'Cancelar'):
      opcao = 0
    self.close()
    return opcao

  def filtro_categoria(self):
    #opcoes = ['[1] Ver Produtos Disponíveis','[2] Comprar um Produto Agora','[3] Voltar ao Menu Anterior', '[4] Finalizar Sessão']
    cabecalho('MENU HISTORICO')
    self.init_opcoes4()
    button, values = self.open()
    if values['1']:
      opcao = 1
    if values['2']:
      opcao = 2
    # cobre os casos de Retornar, fechar janela, ou clicar cancelar
    #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
    if values['0'] or button in (None, 'Cancelar'):
      opcao = 0
    self.close()
    return opcao
  def filtro_cliente(self):
    #opcoes = ['[1] Ver Produtos Disponíveis','[2] Comprar um Produto Agora','[3] Voltar ao Menu Anterior', '[4] Finalizar Sessão']
    cabecalho('MENU HISTORICO')
    self.init_opcoes5()
    button, values = self.open()
    if values['1']:
      opcao = 1
    if values['2']:
      opcao = 2
    # cobre os casos de Retornar, fechar janela, ou clicar cancelar
    #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
    if values['0'] or button in (None, 'Cancelar'):
      opcao = 0
    self.close()
    return opcao



  def init_opcoes(self):
    # sg.theme_previewer()
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text('-------- HISTORICO ----------', font=("Helvica", 25))],
      [sg.Text('Escolha sua opção', font=("Helvica", 15))],
      [sg.Radio('Ver Histórico de Vendas', "RD1", key='1')],
      [sg.Radio('Alterar Histórico de Vendas', "RD1", key='2')],
      [sg.Radio('Incluir uma Venda no Histórico', "RD1", key='3')],
      [sg.Radio('Excluir uma Venda do Histórico', "RD1", key='4')],
      [sg.Radio('Voltar ao Menu Anterior', "RD1", key='5')],
      [sg.Radio('Encerrar Sessão', "RD1", key='6')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema de produtos').Layout(layout)
  def init_opcoes1(self):
    # sg.theme_previewer()
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text('-------- HISTORICO ----------', font=("Helvica", 25))],
      [sg.Text('Escolha sua opção', font=("Helvica", 15))],
      [sg.Radio('Ver Todas as Vendas', "RD1", key='1')],
      [sg.Radio('Aplicar Filtro', "RD1", key='2')],
      [sg.Radio('Voltar ao Menu Anterior', "RD1", key='3')],
      [sg.Radio(' Encerrar Sessão', "RD1", key='4')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema de produtos').Layout(layout)
  def init_opcoes2(self):
    # sg.theme_previewer()
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text('-------- PRODUTOS ----------', font=("Helvica", 25))],
      [sg.Text('Escolha sua opção', font=("Helvica", 15))],
      [sg.Radio('Todas as Cores', "RD1", key='1')],
      [sg.Radio('Escolher uma Cor', "RD1", key='2')],
      [sg.Radio('Encerrar Sessão', "RD1", key='0')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema de produtos').Layout(layout)

  def init_opcoes3(self):
    # sg.theme_previewer()
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text('-------- PRODUTOS ----------', font=("Helvica", 25))],
      [sg.Text('Escolha sua opção', font=("Helvica", 15))],
      [sg.Radio('Todas os Tamanhos', "RD1", key='1')],
      [sg.Radio('Escolher um Tamanho', "RD1", key='2')],
      [sg.Radio('Encerrar Sessão', "RD1", key='0')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema de produtos').Layout(layout)
  def init_opcoes4(self):
    # sg.theme_previewer()
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text('-------- PRODUTOS ----------', font=("Helvica", 25))],
      [sg.Text('Escolha sua opção', font=("Helvica", 15))],
      [sg.Radio('Todas as Categorias', "RD1", key='1')],
      [sg.Radio('Escolher uma Categorias', "RD1", key='2')],
      [sg.Radio('Encerrar Sessão', "RD1", key='0')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema de produtos').Layout(layout)

  def init_opcoes5(self):
    # sg.theme_previewer()
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text('-------- PRODUTOS ----------', font=("Helvica", 25))],
      [sg.Text('Escolha sua opção', font=("Helvica", 15))],
      [sg.Radio('Todos os Clientes', "RD1", key='1')],
      [sg.Radio('Escolher um Cliente', "RD1", key='2')],
      [sg.Radio('Encerrar Sessão', "RD1", key='0')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema de produtos').Layout(layout)
  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def escolha_cor(self):
    print("-------- DADOS COR ----------")
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text('-------- DADOS CATEGORIAS ----------', font=("Helvica", 25))],
      [sg.Text('Cor:', size=(15, 1)), sg.InputText('', key='cor')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]

    ]
    self.__window = sg.Window('Sistema de COR').Layout(layout)

    button, values = self.open()
    cor = values['cor']

    self.close()
    return {"cor": cor }

  def escolha_tamanho(self):
    print("-------- DADOS TAMANHO ----------")
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text('-------- DADOS CATEGORIAS ----------', font=("Helvica", 25))],
      [sg.Text('Tamanho:', size=(15, 1)), sg.InputText('', key='tamanho')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]

    ]
    self.__window = sg.Window('Sistema de Tamanho').Layout(layout)

    button, values = self.open()
    tamanho = values['tamanho']

    self.close()
    return {"tamanho": tamanho }
  def escolha_categoria(self):
    print("-------- DADOS CATEGORIAS ----------")
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text('-------- DADOS CATEGORIAS ----------', font=("Helvica", 25))],
      [sg.Text('Categoria:', size=(15, 1)), sg.InputText('', key='categoria')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]

    ]
    self.__window = sg.Window('Sistema de categorias').Layout(layout)

    button, values = self.open()
    categoria = values['categoria']

    self.close()
    return {"categoria": categoria }

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def imprime_historico_generico(self,produto, quantidade):
    string_todos_produtos = ""
    print("PRODUTO: ", produto.categoria.tipo)
    print("COR: ", produto.cor.nome)
    print("TAMANHO: ", produto.tamanho.descricao)
    print("QUANTIDADE ", quantidade)
    print('\n')

    sg.Popup('-------- LISTA DE HISTORICO ----------', string_todos_produtos)

  def imprime_historico_generico(self, dados_compra, quantidade, nome):
    string_todos_produtos = ""
    print("CLIENTE: ", nome)
    print("PRODUTO: ", dados_compra["categoria"])
    print("COR: ", dados_compra["cor"])
    print("TAMANHO: ", dados_compra["tamanho"])
    print("QUANTIDADE VENDIDA: ", quantidade)

    sg.Popup('-------- LISTA DE HISTORICO ----------', string_todos_produtos)

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def escolha_cor(self):
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text('-------- SELECIONAR PRODUTO ----------', font=("Helvica", 25))],
      [sg.Text('Digite o codigo do produto que deseja selecionar:', font=("Helvica", 15))],
      [sg.Text('codigo:', size=(15, 1)), sg.InputText('', key='codigo')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Seleciona produto').Layout(layout)

    button, values = self.open()
    codigo = values['codigo']
    self.close()
    return codigo

  def mostra_mensagem(self, msg):
    sg.popup("", msg)

  def close(self):
    self.__window.Close()

  def open(self):
    button, values = self.__window.Read()
    return button, values
