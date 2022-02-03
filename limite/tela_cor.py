class TelaCor():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- CORES ----------")
    print("Escolha a opcao")
    print("1 - Incluir Cor")
    print("2 - Alterar Cor")
    print("3 - Listar Cor")
    print("4 - Excluir Cor")
    print("0 - Retornar")


    opcao = int(input("Escolha a opcao: "))
    return opcao

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_cor(self):
    print("-------- DADOS COR ----------")
    nome = input("Nome: ")
    codigo = input("Codigo: ")

    return {"nome": nome, "codigo": codigo}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_cor(self, dados_cor):
    print("NOME DO COR: ", dados_cor["nome"])
    print("CODIGO DO COR: ", dados_cor["codigo"])
    print("\n")

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_cor(self):
    codigo = input("Código do cor que deseja selecionar: ")
    return codigo

  def mostra_mensagem(self, msg):
    print(msg)
