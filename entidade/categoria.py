class Categoria:
    def __init__(self,tipo:str,codigo:int):
        self.__tipo = tipo
        self.__codigo = codigo

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self,tipo:str):
        self.__tipo = tipo

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self,codigo:str):
        self.__codigo = codigo
        
