import socket
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Servico_Remoto.protocolo.request import Request
from Servico_Remoto.protocolo.serializer import serialize_request, deserialize_response

def executar_cliente():
    produto_nome = input("Digite o nome do produto veterinário: ")

    req = Request(produto_nome)
    dados = serialize_request(req)

    with socket.create_connection(('localhost', 5000)) as sock:
        sock.sendall(dados)
        resposta = sock.recv(1024)

    resp = deserialize_response(resposta)

    if resp.status == "OK":
        print(f"\n[Cliente] Produto: {resp.nome}")
        print(f"[Cliente] Preço: R${resp.preco:.2f}")
        print(f"[Cliente] Toxicidade: {resp.toxicidade}")
    else:
        print(f"\n[Cliente] ERRO: {resp.status}")
    
if __name__ == "__main__":
    executar_cliente()