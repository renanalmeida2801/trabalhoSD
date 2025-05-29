import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from OutputStream.produto_quimioterapico_outputStream import ProdutoQuimioterapicoOutputStream
from SubClasses.produto_quimioterapico import ProdutoQuimioterapico

produtos = [
    ProdutoQuimioterapico(1, "Vacina A", "LabVet", 79.9, "Ativo X", "Alta"),
    ProdutoQuimioterapico(2, "Vacina B", "PetLab", 89.5, "Ativo Y", "Baixa")
]

with open("produtos.bin", "wb") as f:
    stream = ProdutoQuimioterapicoOutputStream(produtos, 2, f)
    stream.enviar()