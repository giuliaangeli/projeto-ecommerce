class TelaProduto():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- PRODUTO ----------")
    print("Escolha a opcao")
    print("1 - Fazer Produto")
    print("2 - Listar Produto")
    print("3 - Devolver Produto")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_produto(self):
    print("-------- DADOS PRODUTO ----------")
    nome = input("Nome Cor: ").upper()
    descricao = input("Descricao Tamanho: ").upper()
    tipo = input("Tipo categoria: ").upper()

    return {"nome": nome, "descricao": descricao, "tipo": tipo}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_produto(self, dados_prooduto):
    print("CODIGO DO PRODUTO: ", dados_prooduto["codigo"])
    print("NOME DO COR: ", dados_prooduto["nome_cor"])
   # ("CODIGO DO COR: ", dados_prooduto["codigo_cor"])
    print("DESCRICAO DO TAMANHO: ", dados_prooduto["descricao_tamanho"])
    #print("CODIGO DO TAMANHO: ", dados_prooduto["codigo_tamanho"])
    print("TIPO DO CATEGORIA: ", dados_prooduto["tipo_categoria"])
   # print("CODIGO DO CATEGORIA: ", dados_prooduto["codigo_categoria"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_produto(self):
    codigo = input("Código do produto que deseja selecionar: ")
    return codigo

  def mostra_mensagem(self, msg):
    print(msg)
