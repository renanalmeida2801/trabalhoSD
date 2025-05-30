import socket
import threading
import json

# ==================== Configurações ====================
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000

MULTICAST_GROUP = '224.1.1.1'
MULTICAST_PORT = 6000

# ==================== Notas Multicast ====================
def listen_multicast():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', MULTICAST_PORT))
    mreq = socket.inet_aton(MULTICAST_GROUP) + socket.inet_aton('0.0.0.0')
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    print("[INFO] Aguardando notas informativas...")
    while True:
        data, _ = sock.recvfrom(1024)
        note = json.loads(data.decode())
        if note["type"] == "note":
            print(f"\n[NOTA INFORMATIVA] {note['message']}\n> ", end='')

# ==================== Cliente Principal ====================
def main():
    threading.Thread(target=listen_multicast, daemon=True).start()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_HOST, SERVER_PORT))

        # Login
        login = {"type": "login", "role": "voter"}
        s.send(json.dumps(login).encode())
        print(s.recv(1024).decode())

        # Solicita lista de candidatos
        s.send(json.dumps({"type": "get_candidates"}).encode())
        response = json.loads(s.recv(4096).decode())

        if response["status"] != "ok":
            print("[ERRO]", response["message"])
            return

        candidates = response["candidates"]
        print("\nProdutos disponíveis para votação:")
        for i, c in enumerate(candidates, 1):
            print(f"{i}. {c}")

        try:
            choice = int(input("\nDigite o número do produto que deseja votar: "))
            if 1 <= choice <= len(candidates):
                vote = {"type": "vote", "candidate": candidates[choice - 1]}
                s.send(json.dumps(vote).encode())
                print(s.recv(1024).decode())
            else:
                print("Opção inválida.")
        except ValueError:
            print("Entrada inválida.")

if __name__ == "__main__":
    main()
