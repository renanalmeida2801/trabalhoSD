# Trabalho de Sistemas Distribuídos

Este projeto simula a execução de eventos distribuídos entre 3 processos (P0, P1, P2), abordando três conceitos principais:

1. Relógio Físico (sem sincronização)
2. Relógio Lógico de Lamport
3. Relógios Vetoriais

Cada processo é executado como uma thread e se comunica com os demais por meio de filas internas. O objetivo é demonstrar a necessidade de sincronização lógica entre eventos distribuídos.

---

## ✅ Pré-requisitos

- Python 3.7 ou superior
- Nenhuma biblioteca externa necessária

---

## ▶️ Como Executar

Cada parte é executada separadamente. Rode os arquivos individualmente no terminal:

### 1. Parte 1 – Relógio Físico
```bash
python3 relogio_fisico.py
python3 lamport.py
python3 relogio_vetorial.