from DAOs.dao import DAO
from entidade.historico import Historico
from entidade.usuario import Usuario
from entidade.produto import Produto

#cada entidade terá uma classe dessa, implementação bem simples.
class HistoricoDAO(DAO):
    def __init__(self):
        super().__init__('historico.pkl')

    def add(self, historico: Historico):
        if((historico is not None) and isinstance(historico, Historico) and isinstance(historico.usuario, Usuario) and isinstance(historico.produto, Produto) and isinstance(historico.codigo, int)):
            super().add(historico.usuario, historico.produto,historico.codigo, historico)

    def update(self, historico: Historico):
        if((historico is not None) and isinstance(historico, Historico) and isinstance(historico.usuario, Usuario) and isinstance(historico.produto, Produto) and isinstance(historico.codigo, int)):
            super().update(historico.codigo, historico)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)