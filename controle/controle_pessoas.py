from entidade.adm import Adm
from entidade.usuario import Usuario
from limite.tela_pessoa import TelaPessoa
from limite.tela_abstrata import *


class ControladorPessoa():
    
    def __init__(self, controlador_controladores):
        self.__adms = []
        self.__usuarios = []
        self.__tela_pessoa = TelaPessoa()
        self.__controlador_controladores = controlador_controladores
    
    #condere pelo cpf informado se o usuario ou adm já está nas listas
    def confere_pessoa_cpf(self, tipo_pessoa, cpf):

        #se for adm
        if tipo_pessoa == 1:
            for adm in self.__adms:
                if (adm.cpf == cpf):
                    return adm
            return None
        
        #se for usuario
        else:
            for usuario in self.__usuarios:
                if (usuario.cpf == cpf):
                    return usuario
            return None

    #confere pelo e-mail e senha informados se o usuario ou adm está nas listas
    def confere_pessoa(self, tipo_pessoa: int, email: str, senha: str):
        
        #se for adm
        if tipo_pessoa == 1:
            for adm in self.__adms:
                if(adm.email == email) and (adm.senha == senha):
                    return adm
            return None

        #se for usuário
        else:
            for usuario in self.__usuarios:
                if(usuario.email == email) and (usuario.senha == senha):
                    return usuario
            return None
        
    def incluir_pessoa(self):

        tipo_pessoa = self.__tela_pessoa.adm_ou_usuario

        if tipo_pessoa == 1:
            cpf = self.__tela_pessoa.pega_dado_adm["cpf"]
            adm = self.confere_pessoa_cpf(tipo_pessoa, cpf)

            if adm == None:
                dados_adm = self.__tela_pessoa.pega_dado_adm()
                novo_adm = Adm(dados_adm["nome"], dados_adm["cpf"], dados_adm["telefone"], dados_adm["endereco"], dados_adm["email"], dados_adm["senha"], dados_adm["salario"])
                self.__adms.append(novo_adm)

            else:
                print('Esse CPF já está cadastrado')

        else:
            cpf = self.__tela_pessoa.pega_dados_usuario["cpf"]
            usuario = self.confere_pessoa(tipo_pessoa, cpf)

            if usuario == None:
                dados_usuario = self.__tela_pessoa.pega_dados_usuario()
                novo_usuario = Usuario(dados_usuario["nome"], dados_usuario["cpf"], dados_usuario["telefone"], dados_usuario["endereco"], dados_usuario["email"], dados_usuario["senha"])
                self.__usuarios.append(novo_usuario)
            else:
                print('Esse CPF já está cadastrado')

    def excluir_pessoa(self):
        tipo_pessoa = self.__tela_pessoa.adm_ou_usuario
        email = self.__tela_pessoa.seleciona_pessoa["email"]
        senha = self.__tela_pessoa.seleciona_pessoa["senha"]

        if tipo_pessoa == 1:
            adm = self.confere_pessoa(tipo_pessoa, email, senha)
            if (adm is not None):
                self.__adms.remove(adm)

            else:
                print("ATENÇÃO: esse administrador não está cadastrado")

        else:
            usuario = self.confere_pessoa(tipo_pessoa, email, senha)
            if (usuario is not None):
                self.__adms.remove(usuario)

            else:
                print("ATENÇÃO: esse usuário não está cadastrado")

    def alterar_pessoa(self):
        tipo_pessoa = self.__tela_pessoa.adm_ou_usuario
        email = self.__tela_pessoa.seleciona_pessoa["email"]
        senha = self.__tela_pessoa.seleciona_pessoa["senha"]
        
        if tipo_pessoa == 1:

            adm = self.confere_pessoa(tipo_pessoa, email, senha)
            if (adm is not None):
                novos_dados_adm = self.__tela_pessoa.pega_dado_adm()
                adm.nome = novos_dados_adm["nome"]
                adm.cpf = novos_dados_adm["cpf"]
                adm.telefone = novos_dados_adm["telefone"]
                adm.endereco = novos_dados_adm["endereco"]
                adm.email = novos_dados_adm["email"]
                adm.senha = novos_dados_adm["senha"]
                adm.salario = novos_dados_adm["salario"]

            else:
                print("ATENÇÃO: esse administrador não está cadastrado")

        else:
            usuario = self.confere_pessoa(tipo_pessoa, email, senha)
            if (usuario is not None):
                novos_dados_usuario = self.__tela_pessoa.pega_dado_usuario()
                usuario.nome = novos_dados_usuario["nome"]
                usuario.cpf = novos_dados_usuario["cpf"]
                usuario.telefone = novos_dados_usuario["telefone"]
                usuario.endereco = novos_dados_usuario["endereco"]
                usuario.email = novos_dados_usuario["email"]
                usuario.senha = novos_dados_usuario["senha"]

            else:
                print("ATENÇÃO: esse usuário não está cadastrado")

    def listar_dados(self):
        
        tipo_pessoa = self.__tela_pessoa.adm_ou_usuario
        email = self.__tela_pessoa.seleciona_pessoa["email"]
        senha = self.__tela_pessoa.seleciona_pessoa["senha"]
        
        if tipo_pessoa == 1:
            
            adm = self.confere_pessoa(tipo_pessoa, email, senha)
            if adm is not None:
                cabecalho('ADMINISTRADORES')
                for adm in self.__adms:
                    self.__tela_pessoa.mostra_adm({'nome': adm.nome, 'telefone': adm.telefone})

                cabecalho('USUÁRIOS')
                for usuario in self.__usuarios:
                    self.__tela_pessoa.mostra_usuario({'nome': usuario.nome, 'telefone': usuario.telefone})

        else:
            usuario = self.confere_pessoa(tipo_pessoa, email, senha)

            if usuario is not None:
                cabecalho('SUAS INFORMAÇÕES')
                self.__tela_pessoa.mostra_usuario()
