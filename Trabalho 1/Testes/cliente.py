import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import socket
from SubClasses.produto_quimioterapico import ProdutoQuimioterapico
from OutputStream.produto_quimioterapico_outputStream import ProdutoQuimioterapicoOutputStream

produtos = [
    ProdutoQuimioterapico(3, "Vacina TCP", "VetWorld", 99.9, "X", "Moderada")
]

with socket.create_connection(('localhost', 5000)) as sock:
    stream = sock.makefile('wb')  # converte socket para OutputStream compatível
    out = ProdutoQuimioterapicoOutputStream(produtos, 1, stream)
    out.enviar()
    stream.close()
