class TelaCategoria():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- CATEGORIAS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Categoria")
    print("2 - Alterar Categoria")
    print("3 - Listar Categoria")
    print("4 - Excluir Categoria")
    print("0 - Retornar")


    opcao = int(input("Escolha a opcao: "))
    return opcao

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_categoria(self):
    print("-------- DADOS CATEGORIA ----------")
    tipo = input("Tipo: ").upper()

    return {"tipo": tipo}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_categoria(self, dados_categoria):
    print("TIPO DE CATEGORIA: ", dados_categoria["tipo"])
    print("\n")

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_categoria(self):
    tipo = input("Tipo da categoria que deseja selecionar: ").upper()
    return tipo

  def mostra_mensagem(self, msg):
    print(msg)
