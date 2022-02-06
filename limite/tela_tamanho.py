class TelaTamanho():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- TAMANHO ----------")
    print("Escolha a opcao")
    print("1 - Incluir Tamanho")
    print("2 - Alterar Tamanho")
    print("3 - Listar Tamanho")
    print("4 - Excluir Tamanho")
    print("0 - Retornar")


    opcao = int(input("Escolha a opcao: "))
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
