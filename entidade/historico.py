
class Historico:
    def __init__(self, usuario, produto):
        self.__usuario =  usuario
        self.__compra = produto

    @property
    def usuario(self):
        return self.__usuario

    @property
    def compra(self):
        return self.__compra

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario =  usuario

    @compra.setter
    def compra(self, compra):
        self.__compra = compra