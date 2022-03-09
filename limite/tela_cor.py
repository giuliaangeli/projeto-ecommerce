from limite.tela_abstrata import *

class TelaCor():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    opcoes = ['[1] Incluir Cor','[2] Alterar Cor','[3] Listar Cores', '[4] Excluir Cor', '[5] Voltar ao Menu Anterior', '[6] Sair']
    
    for item in opcoes:
        print(item)

    print(linha())

    opcao = leiaInt('Digite sua opção: ')
    return opcao

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
