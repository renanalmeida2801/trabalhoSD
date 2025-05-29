from Sockets_Streams.SuperClasse.produto import Produto

class ProdutoVeterinario(Produto):
    def __init__(self, id:int, nome:str, fabricante:str, preco:float, principio_ativo:str):
        super().__init__(id, nome, fabricante, preco)
        self.principio_ativo = principio_ativo
        