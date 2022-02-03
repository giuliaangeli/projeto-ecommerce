class Tamanho:
    def __init__(self,descricao:str,codigo:int):
        self.__descricao = descricao
        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self,descricao:str):
        self.__descricao = descricao

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self,codigo:int):
        self.__codigo = codigo
        
