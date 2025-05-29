from produto_biologico import ProdutoBiologico

class VacinaNaoPerecivel(ProdutoBiologico):
    def __init__(self, id:int, nome:str, fabricante:str, preco:float, principio_ativo:str, organismo:str):
        super().__init__(id, nome, fabricante, preco, principio_ativo, organismo)