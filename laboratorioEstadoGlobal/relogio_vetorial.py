import threading
import time
import random
from queue import Queue

NUM_PROCESSES = 3
message_queues = [Queue() for _ in range(NUM_PROCESSES)]
vector_clocks = [[0]*NUM_PROCESSES for _ in range(NUM_PROCESSES)]

def process(pid: int):
    for _ in range(5):
        time.sleep(random.uniform(0.5, 1.5))
        
        # Evento local
        vector_clocks[pid][pid] += 1
        print(f"[P{pid}] Evento local | V = {vector_clocks[pid]}")
        
        # Enviar mensagem
        receiver = random.choice([p for p in range(NUM_PROCESSES) if p != pid])
        message = (pid, list(vector_clocks[pid]))  # Envia uma cópia
        message_queues[receiver].put(message)
        print(f"[P{pid}] Enviou para P{receiver} | V = {vector_clocks[pid]}")

        # Receber mensagens
        while not message_queues[pid].empty():
            sender, recv_vector = message_queues[pid].get()
            for j in range(NUM_PROCESSES):
                vector_clocks[pid][j] = max(vector_clocks[pid][j], recv_vector[j])
            vector_clocks[pid][pid] += 1
            print(f"[P{pid}] Recebeu de P{sender} | V = {vector_clocks[pid]}")

threads = [threading.Thread(target=process, args=(i,)) for i in range(NUM_PROCESSES)]
for t in threads:
    t.start()
for t in threads:
    t.join()
