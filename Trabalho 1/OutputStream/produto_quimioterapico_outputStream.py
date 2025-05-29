import struct
from typing import List
import io
from SubClasses.produto_quimioterapico import ProdutoQuimioterapico

class ProdutoQuimioterapicoOutputStream:
    def __init__(self, produtos: List[ProdutoQuimioterapico], quantidade:int, destino:io.BufferedWriter):
        self.produtos = produtos
        self.quantidade = quantidade
        self.destino = destino
    
    def enviar(self):
        for i in range(min(self.quantidade, len(self.produtos))):
            p = self.produtos[i]
            
            nome_bytes = p.nome.encode('utf-8')
            preco_bytes = struct.pack('f', p.preco)
            tox_bytes = p.toxicidade.encode('utf-8')

            nome_len = struct.pack('i', len(nome_bytes))
            tox_len = struct.pack('i', len(tox_bytes))

            total_bytes = len(nome_len) + len(nome_bytes) + len(preco_bytes) + len(tox_len) + len(tox_bytes)
            self.destino.write(struct.pack('i', total_bytes))

            self.destino.write(nome_len)
            self.destino.write(nome_bytes)
            self.destino.write(preco_bytes)
            self.destino.write(tox_len)
            self.destino.write(tox_bytes)

        self.destino.flush()