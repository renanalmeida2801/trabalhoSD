import threading
import time
import random
from queue import Queue

NUM_PROCESSES = 3
messages_queues = [Queue() for _ in range(NUM_PROCESSES)]

def current_millis():
    return int(time.time() * 1000)

def process(pid: int):
    for i in range(5):
        time.sleep(random.uniform(0.5,1.5))
    
    receiver = random.choice([p for p in range(NUM_PROCESSES) if p != pid])
    timestamp = current_millis()
    message = (pid, timestamp)
    messages_queues[receiver].put(message)
    print(f"[P{pid}] Enviou para P{receiver} às {timestamp}ms")

    while not messages_queues[pid].empty():
        sender, ts = messages_queues[pid].get()
        print(f"P{pid} Recebeu de P{sender} com timestamp físico {ts}ms")

threads = [threading.Thread(target=process, args=(i,)) for i in range(NUM_PROCESSES)]
for t in threads:
    t.start()
for t in threads:
    t.join() 