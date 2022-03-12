class JaCadastrado(Exception):
    def __init__(self):
        super().__init__("Já está cadastrado!")
