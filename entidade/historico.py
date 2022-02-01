class Historico:
    def __init__(self, usuario, compras):
        self.__usuario =  usuario
        self.__compras = list

    @property
    def usuario(self):
        return self.__usuario

    @property
    def compras(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario =  usuario

    @compras.setter
    def compras(self, compras):
        self.__compras = compras