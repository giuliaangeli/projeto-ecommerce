from limite.tela_abstrata import *

class TelaCor():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    cabecalho('MENU CORES')
    opcoes = ['[1] Incluir Cor','[2] Alterar Cor','[3] Listar Cores', '[4] Excluir Cor', '[5] Voltar ao Menu Anterior', '[6] Sair']
    
    for item in opcoes:
        print(item)

    print(linha())

    while True:
      try:
        opcao = leiaInt('Digite sua opção: ')
        if ( opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6):
          raise ValueError
        return opcao        
      except ValueError:
        print("O valor digitado deve ser um inteiro de 1 a 6")



  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_cor(self):
    print("-------- DADOS COR ----------")
    nome = input("Nome: ").upper()
    nome = nome.strip()

    return nome

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_cor(self, dados_cor):
    print(dados_cor["nome"])

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_cor(self):
    nome = input("Nome da cor que deseja selecionar: ").upper()
    nome = nome.strip()
    return nome

  def mostra_mensagem(self, msg):
    print(msg)

  def cabecalho_cores_cadastradas(self):
    cabecalho('CORES CADASTRADAS')
