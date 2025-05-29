import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from Sockets_Streams.SubClasses.produto_quimioterapico import ProdutoQuimioterapico
from Sockets_Streams.OutputStream.produto_quimioterapico_outputStream import ProdutoQuimioterapicoOutputStream

produtos = [
    ProdutoQuimioterapico(1, "Vacina A", "LabVet", 79.9, "Ativo X", "Alta"),
    ProdutoQuimioterapico(2, "Vacina B", "PetLab", 89.5, "Ativo Y", "Baixa")
]

stream = ProdutoQuimioterapicoOutputStream(produtos, 2, sys.stdout.buffer)
stream.enviar()