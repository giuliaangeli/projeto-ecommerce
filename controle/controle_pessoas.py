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

    def confere_adm_email(self, email):

        for adm in self.__adms:
            if (adm.email == email):
                return adm
        return None
        
    def confere_usuario_cpf(self, cpf):

            for usuario in self.__usuarios:
                if (usuario.cpf == cpf):
                    return usuario
            return None

    def confere_usuario_email(self, email):

        for usuario in self.__usuarios:
            if (usuario.email == email):
                return usuario
        return None

    def confere_usuario_cpf_historico(self):
        print('Qual o CPF do usuário?')
        cpf = self.__tela_pessoa.pega_cpf()
        for usuario in self.__usuarios:
            if (usuario.cpf == cpf):
                return usuario
            else:
                print('ATENÇÃO: o CPF informado não corresponde a nenhum cadastrado, digite um CPF válido!')
                self.confere_usuario_cpf_historico()
                
                
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
        usuario_cpf = self.confere_usuario_cpf(dados_novo_usuario["cpf"])
        usuario_email = self.confere_usuario_email(dados_novo_usuario["email"])
        if usuario_cpf == None and usuario_email == None:
            novo_usuario = Usuario(dados_novo_usuario["nome"], dados_novo_usuario["cpf"], dados_novo_usuario["telefone"], dados_novo_usuario["endereco"], dados_novo_usuario["email"], dados_novo_usuario["senha"])
            self.__usuarios.append(novo_usuario)
            print('Seu cadastro foi realizado com sucesso!')
            return novo_usuario
        else:
            print('ATENÇÃO: O CPF ou o e-mail digitado já estão cadastrados')
            return None
        
    def incluir_adm(self):
        dados_novo_adm = self.__tela_pessoa.pega_dado_adm()
        adm_cpf = self.confere_adm_cpf(dados_novo_adm["cpf"])
        adm_email = self.confere_adm_email(dados_novo_adm["email"])
        if adm_cpf == None and adm_email == None:
            novo_adm = Adm(dados_novo_adm["nome"], dados_novo_adm["cpf"], dados_novo_adm["telefone"], dados_novo_adm["endereco"], dados_novo_adm["email"], dados_novo_adm["senha"], dados_novo_adm["salario"])
            self.__adms.append(novo_adm)
            print('Administrador adicionado com sucesso!')

        else:
            print('ATENÇÃO: O CPF ou o e-mail digitado já estão cadastrados')

    def excluir_pessoa(self, pessoa, tipo_pessoa_excluir):
        
        #tipo_pessoa_excluir diz qual lista que será varrida
        #tipo_pessoa_excluir = 1 -> adm
        #tipo_pessoa_excluir = 2 -> usuario
        
        if isinstance(pessoa, Adm):

            if tipo_pessoa_excluir == 1:
                cabecalho('DIGITE O CPF DO ADM QUE DESEJA EXCLUIR')
                cpf = self.__tela_pessoa.pega_cpf()
                for adm in self.__adms:
                    if adm.cpf == cpf:
                        self.__adms.remove(adm)
                        print('Administrador removido!')
                        adm = True
                if adm == False:
                    print("ATENÇÃO: esse administrador não está cadastrado")

            else:
                cabecalho('DIGITE O CPF DO USUÁRIO QUE DESEJA EXCLUIR')
                cpf = self.__tela_pessoa.pega_cpf()
                for usuario in self.__usuarios:
                    if usuario.cpf == cpf:
                        self.__usuarios.remove(usuario)
                        print('Usuário removido!')
                        usuario = True
            
                if usuario == False:
                    print("ATENÇÃO: esse usuário não está cadastrado")

        elif isinstance(pessoa, Usuario):
            self.__usuarios.remove(pessoa)
            print("ATENÇÃO: sua conta foi excluida!")
            exit(0)

    def alterar_pessoa(self, pessoa):
        
        if isinstance(pessoa, Adm):
        
            novos_dados_adm = self.__tela_pessoa.pega_dado_adm()
            pessoa.nome = novos_dados_adm["nome"]
            pessoa.cpf = novos_dados_adm["cpf"]
            pessoa.telefone = novos_dados_adm["telefone"]
            pessoa.endereco = novos_dados_adm["endereco"]
            pessoa.email = novos_dados_adm["email"]
            pessoa.senha = novos_dados_adm["senha"]
            pessoa.salario = novos_dados_adm["salario"]
            print('\n Dados alterados com sucesso!\n')

        elif isinstance(pessoa, Usuario):
            
            novos_dados_usuario = self.__tela_pessoa.pega_dados_usuario()
            pessoa.nome = novos_dados_usuario["nome"]
            pessoa.cpf = novos_dados_usuario["cpf"]
            pessoa.telefone = novos_dados_usuario["telefone"]
            pessoa.endereco = novos_dados_usuario["endereco"]
            pessoa.email = novos_dados_usuario["email"]
            pessoa.senha = novos_dados_usuario["senha"]
            print('\nDados alterados com sucesso!')

    def listar_dados(self, pessoa, funcao = 0):

        #funcao é o parametro que define o que será impresso
        #funcao = 1 -> imprime os dados dos administradores
        #funcao = 2 -> imprime os dados dos usuários

        if isinstance(pessoa, Adm):

            if funcao == 1:
                cabecalho('ADMINISTRADORES')
                for adm in self.__adms:
                    self.__tela_pessoa.mostra_adm({"nome": adm.nome, "cpf": adm.cpf, "telefone": adm.telefone, "endereco": adm.endereco, "email": adm.email, "senha": adm.senha, "salario": adm.salario})

            elif funcao == 2:
                cabecalho('USUÁRIOS')
                for usuario in self.__usuarios:
                    self.__tela_pessoa.mostra_usuario({"nome": usuario.nome, "cpf": usuario.cpf, "telefone": usuario.telefone, "endereco": usuario.endereco, "email": usuario.email, "senha": usuario.senha})

        elif isinstance(pessoa, Usuario):

            cabecalho('SUAS INFORMAÇÕES')
            self.__tela_pessoa.mostra_usuario({"nome": pessoa.nome, "cpf": pessoa.cpf, "telefone": pessoa.cpf, "endereco": pessoa.endereco, "email": pessoa.email, "senha": pessoa.senha})

    def retornar_menu_adm(self, adm):
        self.__controlador_sistema.controla_menu_principal_adm(adm)

    def retornar_menu_usuario(self, usuario):
        self.__controlador_sistema.controla_menu_principal_usuario(usuario)

    def abre_tela_adm(self, adm):

        lista_opcoes = {1: self.incluir_adm, 2: self.excluir_pessoa, 3: self.listar_dados, 4: self.alterar_pessoa , 5: self.incluir_usuario, 6: self.excluir_pessoa, 7: self.listar_dados , 8: self.retornar_menu_adm, 9: self.__controlador_sistema.abre_tela_inicial}

        continua = True
        while continua:
            opcao_escolhida = self.__tela_pessoa.tela_pessoa_adm()
            if opcao_escolhida == 2 or opcao_escolhida == 3:
                lista_opcoes[opcao_escolhida](adm,1)
            elif opcao_escolhida == 4 or opcao_escolhida == 8:
                lista_opcoes[opcao_escolhida](adm)
            elif opcao_escolhida == 6 or opcao_escolhida == 7:
                lista_opcoes[opcao_escolhida](adm,2)
            else:
                lista_opcoes[opcao_escolhida]()
    
    def abre_tela_usuario(self, usuario):
    
        lista_opcoes = {1: self.listar_dados, 2: self.alterar_pessoa , 3: self.excluir_pessoa, 4: self.retornar_menu_usuario, 5: self.__controlador_sistema.abre_tela_inicial}

        continua = True
        while continua:
            opcao_escolhida = self.__tela_pessoa.tela_pessoa_usuario()
            if opcao_escolhida == 3:
                lista_opcoes[opcao_escolhida](usuario, 2)
            elif opcao_escolhida == 5:
                lista_opcoes[opcao_escolhida]()
            else:
                lista_opcoes[opcao_escolhida](usuario)
    
    def instancia_pessoas(self):

        #Instanciando 2 adms na lista
        adm1 = Adm('Giulia Angeli','09641787969','47997930839','João Pio Duarte Silva','giulia@gmail.com','1234','5000')
        adm2 = Adm('Guilherme Ferreira','99900011199','13996893954','Lauro Linhares','guilherme@gmail.com','1234','5000')
        adm3 = Adm('Guilherme Ferreira','1','111','111','1','1','5000')
        self.__adms.append(adm1)
        self.__adms.append(adm2)
        self.__adms.append(adm3)

        #Instanciando 2 clientes na lista
        usuario1 = Usuario('Giulia Angeli','09641787969','47997930839','João Pio Duarte Silva','giulia@gmail.com','1234')
        usuario2 = Usuario('Guilherme Ferreira','99900011199','13996893954','Lauro Linhares','guilherme@gmail.com','1234')
        self.__usuarios.append(usuario1)
        self.__usuarios.append(usuario2)
