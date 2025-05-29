import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import socket
from Sockets_Streams.InputStream.produto_quimioterapico_inputstream import ProdutoQuimioterapicoInputStream

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(('localhost', 5000))
    server.listen()
    print("Servidor aguardando conexão...")

    conn, addr = server.accept()
    with conn:
        print(f"conectado com {addr}")
        origem = conn.makefile('rb')
        stream = ProdutoQuimioterapicoInputStream(origem)
        produtos = stream.ler_produtos()

        for p in produtos:
            print(f"Produto: {p.nome}, Preço: {p.preco}, Toxicidade: {p.toxicidade}")
