class Carrinho:
    def __init__(self, itens):
        self.__itens = list

    @property
    def itens(self):
        return self.__itens

    @itens.setter
    def itens(self, itens):
        self.__itens = list
