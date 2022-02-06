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
    nome = input("Nome: ").upper()

    return {"nome": nome}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_cor(self, dados_cor):
    print("NOME DO COR: ", dados_cor["nome"])
    print("\n")

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_cor(self):
    nome = input("Nome da cor que deseja selecionar: ").upper()
    return nome

  def mostra_mensagem(self, msg):
    print(msg)
