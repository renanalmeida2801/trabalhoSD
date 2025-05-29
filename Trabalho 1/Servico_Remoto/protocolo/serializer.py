import struct
from Servico_Remoto.protocolo.request import Request
from Servico_Remoto.protocolo.response import Response

def serialize_request(req:Request) ->bytes:
    nome_bytes = req.produto_nome.encode('utf-8')
    return struct.pack('i', len(nome_bytes)) + nome_bytes

def deserialize_request(data:bytes) -> Request:
    nome_len = struct.unpack('i', data[:4])[0]
    nome = data[4:4+nome_len].decode('utf-8')
    return Request(nome)

def serialize_response(resp:Response) -> bytes:
    nome_b = resp.nome.encode('utf-8')
    tox_b = resp.toxicidade.encode('utf-8')
    status_b = resp.status.encode('utf-8')
    return(
        struct.pack('i', len(nome_b)) + nome_b +
        struct.pack('f', resp.preco) +
        struct.pack('i', len(tox_b)) + tox_b +
        struct.pack('i', len(status_b)) + status_b
    )

def deserialize_response(data:bytes) -> Response:
    idx = 0
    nome_len = struct.unpack('i', data[idx:idx+4])[0]
    idx += 4
    nome = data[idx:idx+nome_len].decode('utf-8')
    idx += nome_len

    preco = struct.unpack('f', data[idx:idx+4])[0]
    idx += 4

    tox_len = struct.unpack('i', data[idx:idx+4])[0]
    idx += 4
    toxicidade = data[idx:idx+tox_len].decode('utf-8')
    idx += tox_len

    status_len = struct.unpack('i', data[idx:idx+4])[0]
    idx += 4
    status = data[idx:idx+status_len].decode('utf-8')

    return Response(nome, preco, toxicidade, status)