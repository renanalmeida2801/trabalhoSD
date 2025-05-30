import socket
import json

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_HOST, SERVER_PORT))

        # Login como administrador
        login = {"type": "login", "role": "admin"}
        s.send(json.dumps(login).encode())
        print(s.recv(1024).decode())

        while True:
            print("\n=== Menu Administrador ===")
            print("1. Adicionar candidato")
            print("2. Remover candidato")
            print("3. Enviar nota informativa")
            print("4. Listar historico de açoes")
            print("5. Sair")

            choice = input("Escolha: ").strip()

            if choice == '1':
                name = input("Nome do candidato (produto): ").strip()
                desc = input("Descrição: ").strip()
                request = {"type": "add_candidate", "candidate": name, "description": desc}
                s.send(json.dumps(request).encode())
                response = json.loads(s.recv(1024).decode())
                print(response.get("message", "Resposta desconhecida."))

            elif choice == '2':
                name = input("Nome do candidato (produto) a remover: ").strip()
                request = {"type": "remove_candidate", "candidate": name}
                s.send(json.dumps(request).encode())
                response = json.loads(s.recv(1024).decode())
                print(response.get("message", "Resposta desconhecida."))

            elif choice == '3':
                note = input("Digite a nota informativa a enviar: ").strip()
                request = {"type": "note", "message": note}
                s.send(json.dumps(request).encode())
                response = json.loads(s.recv(1024).decode())
                print(response.get("message", "Resposta desconhecida."))
            elif choice == '4':
                note = input("Listar historico de açoes: ").strip() 
                request = {"type": "get_history"}
                s.send(json.dumps(request).encode())
                response = json.loads(s.recv(8192).decode())  # maior buffer para histórico
                if response.get("status") == "ok":
                    print("\n=== Histórico de Ações ===")
                    print("=== Histórico de Ações ===")
                for entry in response.get("history", []):
                    print(f"[{entry['timestamp']}] {entry['action']}: {entry['details']}")

                    history = response.get("history", [])
                    if not history:
                        print("Nenhuma ação registrada.")
                    else:
                        for i, entry in enumerate(history, 1):
                            print(f"{i}. [{entry['timestamp']}] {entry['action']}: {entry['details']}")
                else:
                    print("[ERRO]", response.get("message", "Erro desconhecido."))

            elif choice == '5':
                print("Encerrando sessão do administrador.")
                break

            else:
                print("Opção inválida.")

if __name__ == "__main__":
    main()