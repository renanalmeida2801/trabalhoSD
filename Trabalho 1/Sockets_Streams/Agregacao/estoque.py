class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar(self, produto):
        self.produtos.append(produto)

    def listar(self):
        for p in self.produtos:
            print(f"{p.nome} (RS{p.preco:.2f})")