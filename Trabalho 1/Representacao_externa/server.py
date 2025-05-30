import socket
import threading
import json
import time
import os

# ==================== Configurações ====================
HOST = '127.0.0.1'
PORT = 5000

MULTICAST_GROUP = '224.1.1.1'
MULTICAST_PORT = 6000

VOTING_DURATION = 60  # segundos

DATA_FILE = os.path.join("data", "products.json")
voting_active = True

clients = []
votes = {}
data_lock = threading.Lock()

# ==================== Utilitários ====================
def load_candidates():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_candidates(candidates):
    with open(DATA_FILE, 'w') as f:
        json.dump(candidates, f, indent=2)

def handle_client(conn, addr):
    global voting_active

    print(f"[+] Nova conexão: {addr}")
    try:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break

            request = json.loads(data)

            if request["type"] == "login":
                role = request["role"]
                if role == "admin":
                    conn.send(json.dumps({"status": "ok", "message": "Login de administrador realizado."}).encode())
                else:
                    conn.send(json.dumps({"status": "ok", "message": "Login de eleitor realizado."}).encode())

            elif request["type"] == "get_candidates":
                candidates = load_candidates()
                conn.send(json.dumps({"status": "ok", "candidates": list(candidates.keys())}).encode())

            elif request["type"] == "vote":
                if not voting_active:
                    conn.send(json.dumps({"status": "error", "message": "Votação encerrada."}).encode())
                    continue

                candidate = request["candidate"]
                with data_lock:
                    if candidate in votes:
                        votes[candidate] += 1
                    else:
                        votes[candidate] = 1
                conn.send(json.dumps({"status": "ok", "message": f"Voto registrado para {candidate}."}).encode())

            elif request["type"] == "add_candidate":
                candidate = request["candidate"]
                desc = request["description"]
                candidates = load_candidates()
                if candidate in candidates:
                    conn.send(json.dumps({"status": "error", "message": "Candidato já existe."}).encode())
                else:
                    candidates[candidate] = {"description": desc}
                    save_candidates(candidates)
                    conn.send(json.dumps({"status": "ok", "message": "Candidato adicionado."}).encode())

            elif request["type"] == "remove_candidate":
                candidate = request["candidate"]
                candidates = load_candidates()
                if candidate in candidates:
                    del candidates[candidate]
                    save_candidates(candidates)
                    conn.send(json.dumps({"status": "ok", "message": "Candidato removido."}).encode())
                else:
                    conn.send(json.dumps({"status": "error", "message": "Candidato não encontrado."}).encode())

            elif request["type"] == "note":
                message = request["message"]
                send_multicast_note(message)
                conn.send(json.dumps({"status": "ok", "message": "Nota enviada via multicast."}).encode())

    except Exception as e:
        print(f"[ERRO] Cliente {addr}: {e}")
    finally:
        conn.close()
        print(f"[-] Conexão encerrada: {addr}")

def send_multicast_note(message):
    multicast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    multicast_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    data = json.dumps({"type": "note", "message": message})
    multicast_socket.sendto(data.encode(), (MULTICAST_GROUP, MULTICAST_PORT))
    multicast_socket.close()

def end_voting():
    global voting_active  # ✅ Correção aqui

    if not voting_active:
        return

    voting_active = False
    print("\n[VOTAÇÃO ENCERRADA] Calculando resultados...")

    with data_lock:
        total = sum(votes.values())
        if total == 0:
            print("Nenhum voto recebido.")
        else:
            print("RESULTADOS:")
            for candidate, count in votes.items():
                percent = (count / total) * 100
                print(f"- {candidate}: {count} votos ({percent:.2f}%)")
            winner = max(votes.items(), key=lambda item: item[1])[0]
            print(f"\n🏆 Candidato vencedor: {winner}")

def voting_timer():
    time.sleep(VOTING_DURATION)
    end_voting()

# ==================== Execução Principal ====================
def start_server():
    print("[INICIANDO SERVIDOR]")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"[ESPERANDO CONEXÕES] Servidor escutando em {HOST}:{PORT}")

    threading.Thread(target=voting_timer, daemon=True).start()

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
