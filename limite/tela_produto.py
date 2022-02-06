from limite.tela_abstrata import *

class TelaProduto():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_produtos_inicial_adm(self):
    cabecalho('ESCOLHA UMA OPÇÃO')
    opcoes = ['[1] Incluir Produto','[2] Listar Produtos','[3] Alterar Produto', '[4] Excluir Produto', '[5] Voltar ao Menu Anterior', '[6] Finalizar Sessão']
    
    for item in opcoes:
        print(item)

    print(linha())

    opcao = leiaInt('Digite sua opção: ')
    return opcao

  def tela_produtos__adm(self):
    cabecalho('ESCOLHA UMA OPÇÃO')
    opcoes = ['[1] Incluir Produto Agora','[2] Menu Cor','[3] Menu Tamanho', '[4] Menu Categoria', '[5] Voltar ao Menu Anterior', '[6] Finalizar Sessão']
    
    for item in opcoes:
        print(item)

    print(linha())

    opcao = leiaInt('Digite sua opção: ')
    return opcao

  def tela_produto_usuario(self):
    cabecalho('ESCOLHA UMA OPÇÃO')
    opcoes = ['[1] Ver Produtos Disponíveis','[2] Comprar um Produto Agora','[3] Voltar ao Menu Anterior', '[4] Finalizar Sessão']
    
    for item in opcoes:
        print(item)

    print(linha())

    opcao = leiaInt('Digite sua opção: ')
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
