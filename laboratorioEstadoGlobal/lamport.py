import threading
import time
import random
from queue import Queue

NUM_PROCESSES = 3
messages_queue = [Queue() for _ in range(NUM_PROCESSES)]
logical_clocks =[0 for _ in range(NUM_PROCESSES)]

def process(pid: int):
    global logical_clocks
    for i in range(5):
        time.sleep(random.uniform(0.5, 1.5))

        logical_clocks[pid] += 1
        print(f"[P{pid}] Evento interno | L({pid}) = {logical_clocks[pid]}")

        receiver = random.choice([p for p in range(NUM_PROCESSES) if p != pid])
        timestamp = logical_clocks[pid]
        messages_queue[receiver].put((pid, timestamp))
        print(f"[P{pid}] Enviou para P{receiver} | L({pid}) = {timestamp}")

        while not messages_queue[pid].empty():
            sender, recv_clock = messages_queue[pid].get()
            logical_clocks[pid] = max(logical_clocks[pid], recv_clock) + 1
            print(f"[P{pid}] Recebeu de P{sender} (L={recv_clock}) | Novo L({pid}) = {logical_clocks[pid]}")

threads = [threading.Thread(target=process, args=(i,)) for i in range(NUM_PROCESSES)]
for t in threads:
    t.start()
for t in threads:
    t.join()