from entidade.adm import Adm
from entidade.usuario import Usuario
from limite.tela_pessoa import TelaPessoa


class ControladorPessoa():
    
    def __init__(self, controlador_controladores):
        self.__adms = []
        self.__usuarios = []
        self.__tela_pessoa = TelaPessoa()
        self.__controlador_controladores = controlador_controladores

    def incluir_adm(self):
        dados_adm = self.__tela_pessoa.pega_dado_adm
        adm = Adm(dados_adm["nome"], dados_adm["cpf"], dados_adm["telefone"], dados_adm["endereco"], dados_adm["email"], dados_adm["senha"], dados_adm["salario"])
        self.__adms.append(adm)

    def incluir_usuario(self):
        dados_usuario = self.__tela_pessoa.pega_dados_usuario
        usuario = Usuario(dados_usuario["nome"], dados_usuario["cpf"], dados_usuario["telefone"], dados_usuario["endereco"], dados_usuario["email"], dados_usuario["senha"])
        self.__usuarios.append(usuario)        
        