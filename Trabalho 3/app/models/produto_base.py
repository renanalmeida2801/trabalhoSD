from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4

class ProdutoBase(BaseModel):
    id: UUID = uuid4()
    nome: str
    fabricante: str
    preco: float
    quantidade: int

    class Config:
        orm_mode = True