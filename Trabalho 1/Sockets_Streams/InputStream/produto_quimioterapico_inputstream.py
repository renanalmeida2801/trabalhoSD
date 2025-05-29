import struct
import io
from Sockets_Streams.SubClasses.produto_quimioterapico import ProdutoQuimioterapico

class ProdutoQuimioterapicoInputStream:
    def __init__(self, origem: io.BufferedReader):
        """
        :param origem: InputStream (arquivo, sys.stdin.buffer ou socket.makefile('rb'))
        """
        self.origem = origem

    def ler_produtos(self):
        produtos = []

        while True:
            total_raw = self.origem.read(4)
            if not total_raw:
                break
            total_bytes = struct.unpack('i', total_raw)[0]

            nome_len = struct.unpack('i', self.origem.read(4))[0]
            nome = self.origem.read(nome_len).decode('utf-8')

            preco = struct.unpack('f', self.origem.read(4))[0]

            tox_len = struct.unpack('i', self.origem.read(4))[0]
            toxicidade = self.origem.read(tox_len).decode('utf-8')

            produto = ProdutoQuimioterapico(
                id=0,
                nome=nome,
                fabricante="(desconhecido)",
                preco= preco,
                principio_ativo="(desconhecido)",
                toxicidade=toxicidade
            )
            produtos.append(produto)
        return produtos