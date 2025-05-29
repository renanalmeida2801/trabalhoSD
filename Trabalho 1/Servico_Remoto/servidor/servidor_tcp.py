import socket
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Servico_Remoto.protocolo.serializer import deserialize_request, serialize_response
from Servico_Remoto.protocolo.response import Response
from Sockets_Streams.SubClasses.produto_quimioterapico import ProdutoQuimioterapico


banco_produtos = {
    "Vacina TCP": ProdutoQuimioterapico(1, "Vacina TCP", "VetWorld", 99.9, "X", "Moderada"),
    "Vacina Extra": ProdutoQuimioterapico(2, "Vacina Extra", "PetLab", 109.5, "Y", "Alta"),
}

def iniciar_servidor(host='localhost', porta=5000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.bind((host, porta))
        servidor.listen()
        print(f"[Servidor] Escutando em {host}:{porta}...")

        conn, addr = servidor.accept()
        with conn:
            print(f"[Servidor] Conexao de {addr}")

            dados = conn.recv(1024)
            if not dados:
                print("[Servidor] Nenhum dado recebido.")
                return
            
            req = deserialize_request(dados)
            print(f"[Servidor] Pedido: {req.produto_nome}")

            produto = banco_produtos.get(req.produto_nome)

            if produto:
                resp = Response(produto.nome, produto.preco, produto.toxicidade, "OK")
            else:
                resp = Response("Desconhecido", 0.0, "Desconhecido", "ERRO: Produto não encontrado")
            
            conn.sendall(serialize_response(resp))
            print("[Servidor] Resposta enviada.")

if __name__ == "__main__":
    iniciar_servidor()
