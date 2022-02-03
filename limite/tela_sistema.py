class TelaSistema:
    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("-------- Sis ---------")
        print("Escolha sua opcao")
        print("1 - CORES")
        print("2 - TAMANHOS")
        print("3 - CATEGORIAS")
        print("4 - PRODUTOS")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao:"))
        return opcao
