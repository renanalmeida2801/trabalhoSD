
import json


def send_json(sock, data):
    sock.sendall(json.dumps(data).encode())


def recv_json(sock):
    return json.loads(sock.recv(4096).decode())


## ===== data/products.json =====
# Salve este conteúdo como data/products.json
# {
#     "Vermífugo X": {"description": "Combate vermes intestinais."},
#     "Antibiótico Y": {"description": "Trata infecções bacterianas."}
# }
