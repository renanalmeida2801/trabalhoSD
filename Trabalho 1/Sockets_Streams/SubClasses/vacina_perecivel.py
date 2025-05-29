from Sockets_Streams.SubClasses.produto_biologico import ProdutoBiologico
from Sockets_Streams.Interface.perecivel import Perecivel

class VacinaPerecivel(ProdutoBiologico, Perecivel):
    def __init__(self, id:int, nome:str, fabricante:str, preco:float, principio_ativo:str, organismo:str, validade:str):
        super().__init__(id, nome, fabricante, preco, principio_ativo, organismo)
        self.validade = validade

    def esta_vencido(self, data_atual:str) -> bool:
        return self.validade < data_atual