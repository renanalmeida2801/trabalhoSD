from Sockets_Streams.SubClasses.produto_veterinario import ProdutoVeterinario

class ProdutoQuimioterapico(ProdutoVeterinario):
    def __init__(self, id:int, nome:str, fabricante:str, preco:float, principio_ativo:str, toxicidade:str):
        super().__init__(id, nome, fabricante, preco, principio_ativo)
        self.toxicidade = toxicidade