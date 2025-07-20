from datetime import date
from .produto_biologico import ProdutoBiologico

class VacinaPerecivel(ProdutoBiologico):
    validade: date