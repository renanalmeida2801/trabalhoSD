import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import socket
from Sockets_Streams.SubClasses.produto_quimioterapico import ProdutoQuimioterapico
from Sockets_Streams.OutputStream.produto_quimioterapico_outputStream import ProdutoQuimioterapicoOutputStream

produtos = [
    ProdutoQuimioterapico(3, "Vacina TCP", "VetWorld", 99.9, "X", "Moderada"),
    ProdutoQuimioterapico(4, "Vacina Extra", "AnimalPharm", 109.5, "Y", "Alta")
]

with socket.create_connection(('localhost', 5000)) as sock:
    stream = sock.makefile('wb')
    out = ProdutoQuimioterapicoOutputStream(produtos, 2, stream)
    out.enviar()
    stream.close()
