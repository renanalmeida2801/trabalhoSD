from typing import List, Union
from .produto_quimioterapico import ProdutoQuimioterapico
from .vacina_perecivel import VacinaPerecivel
from .vacina_nao_perecivel import VacinaNaoPerecivel

class Estoque:
    def __init__(self):
        self.produtos: List[
            Union[ProdutoQuimioterapico, VacinaPerecivel, VacinaNaoPerecivel]
        ] = []
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        return self.produtos
    
    def listar_pereciveis(self):
        return [p for p in self.produtos if hasattr(p, "validade")]