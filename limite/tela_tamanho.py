from limite.tela_abstrata import *

class TelaTamanho():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    cabecalho('MENU TAMANHO')
    opcoes = ['[1] Incluir Tamanho','[2] Alterar Tamanho','[3] Listar Tamanho', '[4] Excluir Tamanho', '[5] Voltar ao Menu Anterior', '[6] Sair']
    
    for item in opcoes:
        print(item)
    print(linha())
    while True:
      try:
        opcao = leiaInt('Digite sua opção: ')
        if (opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and != 6):
          raise ValueError
        return opcao        
      except ValueError:
        print("O valor digitado deve ser um inteiro de 1 a 5")

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_tamanho(self):
    print("-------- DADOS TAMANHO ----------")
    descricao = input("Descricao: ").upper()
    descricao = descricao.strip()
    return descricao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_tamanho(self, dados_tamanho):
    print( dados_tamanho["descricao"])
    

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_tamanho(self):
    descricao = input("Descricao do tamanho que deseja selecionar: ").upper()
    descricao = descricao.strip()
    return descricao

  def mostra_mensagem(self, msg):
    print(msg)

  def cabecalho_tamanhos_cadastrados(self):
    cabecalho('TAMANHOS CADASTRADOS')
