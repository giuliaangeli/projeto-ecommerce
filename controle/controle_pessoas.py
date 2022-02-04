from entidade.adm import Adm
from entidade.usuario import Usuario
from limite.tela_pessoa import TelaPessoa
from limite.tela_abstrata import *


class ControladorPessoa():
    
    def __init__(self, controlador_sistema):
        self.__adms = []
        self.__usuarios = []
        self.__tela_pessoa = TelaPessoa()
        self.__controlador_sistema = controlador_sistema
    
    #condere pelo cpf informado se o usuario ou adm já está nas listas
    def confere_adm_cpf(self, cpf):

            for adm in self.__adms:
                if (adm.cpf == cpf):
                    return adm
            return None
        
    def confere_usuario_cpf(self, cpf):

            for usuario in self.__usuarios:
                if (usuario.cpf == cpf):
                    return usuario
            return None

    #confere pelo e-mail e senha informados se o usuario ou adm está nas listas
    def confere_login(self, tipo_pessoa: int):
        dados_login = self.__tela_pessoa.pega_dados_login()

        #se for adm
        if tipo_pessoa == 1:
            for adm in self.__adms:
                if(adm.email == dados_login['email']) and (adm.senha == dados_login['senha']):
                    return adm
            return None

        #se for usuário
        else:
            for usuario in self.__usuarios:
                if(usuario.email == dados_login['email']) and (usuario.senha == dados_login['senha']):
                    return usuario
            return None

    def incluir_usuario(self):

        dados_novo_usuario = self.__tela_pessoa.pega_dados_usuario()
        usuario = self.confere_usuario_cpf(dados_novo_usuario["cpf"])

        if usuario == None:
            novo_usuario = Usuario(dados_novo_usuario["nome"], dados_novo_usuario["cpf"], dados_novo_usuario["telefone"], dados_novo_usuario["endereco"], dados_novo_usuario["email"], dados_novo_usuario["senha"])
            self.__usuarios.append(novo_usuario)
            print('Seu cadastro foi realizado com sucesso!')
        else:
            print('Esse CPF já está cadastrado')
        
    def incluir_adm(self):
        dados_novo_adm = self.__tela_pessoa.pega_dado_adm()
        adm = self.confere_adm_cpf(dados_novo_adm["cpf"])

        if adm == None:
            novo_adm = Adm(dados_novo_adm["nome"], dados_novo_adm["cpf"], dados_novo_adm["telefone"], dados_novo_adm["endereco"], dados_novo_adm["email"], dados_novo_adm["senha"], dados_novo_adm["salario"])
            self.__adms.append(novo_adm)

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
                self.__tela_pessoa.mostra_usuario(usuario)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela_adm(self):

        lista_opcoes = {1: self.incluir_adm, 2: self.alterar_pessoa, 3: self.listar_dados, 4: self.excluir_pessoa, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_pessoa.tela_opcoes()]()
    
    def abre_tela_usuario(self):

        lista_opcoes = {1: self.incluir_usuario, 2: self.alterar_pessoa, 3: self.listar_dados, 4: self.excluir_pessoa, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_pessoa.tela_opcoes()]()
    
    def instancia_pessoas(self):

        #Instanciando 2 adms na lista
        adm1 = Adm('Giulia Angeli','09641787969','47997930839','João Pio Duarte Silva','giulia@gmail.com','1234','5000')
        adm2 = Adm('Guilherme Ferreira','99900011199','13996893954','Lauro Linhares','guilherme@gmail.com','1234','5000')
        self.__adms.append(adm1)
        self.__adms.append(adm2)
        #Instanciando 2 clientes na lista
        usuario1 = Usuario('Giulia Angeli','09641787969','47997930839','João Pio Duarte Silva','giulia@gmail.com','1234')
        usuario2 = Usuario('Guilherme Ferreira','99900011199','13996893954','Lauro Linhares','guilherme@gmail.com','1234')
        self.__usuarios.append(usuario1)
        self.__usuarios.append(usuario2)
