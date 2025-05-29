from Sockets_Streams.SubClasses.produto_veterinario import ProdutoVeterinario

class ProdutoBiologico(ProdutoVeterinario):
    def __init__(self, id:int, nome:str, fabricante:str, preco:float, principio_ativo:str, organismo:str):
        super().__init__(id, nome, fabricante, preco, principio_ativo)
        self.organismo = organismo