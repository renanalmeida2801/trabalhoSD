import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 5000))
    s.listen()
    print("Servidor aguardando conexão...")

    conn, addr = s.accept()
    with conn:
        print(f"Conexão de {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Recebido ({len(data)} bytes):", data)
