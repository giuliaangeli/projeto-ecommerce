from entidade.pessoa import Pessoa


class ControladorPessoa():
    
    def __init__(self, controlador_controladores):
        self._pessoas = []
        self.__tela_pessoa = TelaPessoa()
        self.__controlador_controladores = controlador_controladores

        