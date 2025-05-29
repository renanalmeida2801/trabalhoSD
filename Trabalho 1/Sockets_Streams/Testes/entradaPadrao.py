import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Sockets_Streams.InputStream.produto_quimioterapico_inputstream import ProdutoQuimioterapicoInputStream

stream = ProdutoQuimioterapicoInputStream(sys.stdin.buffer)
produtos = stream.ler_produtos()

for p in produtos:
    print(f"Produto: {p.nome}, Preco: {p.preco}, Toxicidade: {p.toxicidade}")