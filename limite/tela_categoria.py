from limite.tela_abstrata import *

class TelaCategoria():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    cabecalho('MENU CATEGORIA')
    opcoes = ['[1] Incluir Categoria','[2] Alterar Categoria','[3] Listar Categorias', '[4] Excluir Categoria', '[5] Voltar ao Menu Anterior', '[6] Sair']
    
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
  def pega_dados_categoria(self):
    print("-------- DADOS CATEGORIA ----------")
    tipo = input("Tipo: ").upper()
    tipo = tipo.strip()

    return tipo

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_categoria(self, dados_categoria):
    print(dados_categoria["tipo"])

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_categoria(self):
    tipo = input("Tipo da categoria que deseja selecionar: ").upper()
    tipo = tipo.strip()
    return tipo

  def mostra_mensagem(self, msg):
    print(msg)

  def cabecalho_categorias_cadastradas(self):
    cabecalho('TAMANHOS CADASTRADOS')
