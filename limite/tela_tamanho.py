from limite.tela_abstrata import *

class TelaTamanho():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    cabecalho('MENU TAMANHO')
    opcoes = ['[1] Incluir Tamanho','[2] Alterar Tamanho','[3] Listar Tamanho', '[4] Excluir Tamanho', '[5] Voltar ao Menu Anterior', '[6] Sair']
    
    for item in opcoes:
        print(item)

    print(linha())

    opcao = leiaInt('Digite sua opção: ')
    return opcao

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_tamanho(self):
    print("-------- DADOS TAMANHO ----------")
    descricao = input("Descricao: ").upper()

    return {"descricao": descricao}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_tamanho(self, dados_tamanho):
    print("DESCRICAO DO TAMANHO: ", dados_tamanho["descricao"])
    print("\n")

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_tamanho(self):
    descricao = input("Descricao do tamanho que deseja selecionar: ").upper()
    return descricao

  def mostra_mensagem(self, msg):
    print(msg)
