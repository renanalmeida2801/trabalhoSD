class ServicoCadastro:
    def __init__(self, estoque):
        self.estoque = estoque

    def cadastrar_produto(self, produto):
        self.estoque.adcionar(produto)
        print(f"Produto '{produto.nome}' cadastrado com sucesso.")