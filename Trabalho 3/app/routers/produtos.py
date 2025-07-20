from fastapi import APIRouter
from app.database import estoque
from app.models.produto_quimioterapico import ProdutoQuimioterapico
from app.models.vacina_nao_perecivel import VacinaNaoPerecivel
from app.models.vacina_perecivel import VacinaPerecivel
from typing import List, Union

router = APIRouter(prefix="/produtos", tags=["Produtos"])

@router.post("/quimioterapico")
def adicionar_quimioterapico(produto: ProdutoQuimioterapico):
    estoque.adicionar_produto(produto)
    return {"mensagem": "Produto Quimioterápico adicionado com sucesso!"}

@router.post("/vacina_perecivel")
def adicionar_vacina_perecivel(produto: VacinaPerecivel):
    estoque.adicionar_produto(produto)
    return {"mensagem": "Vacina perecível adicionada com sucesso!"}

@router.post("/vacina_nao_perecivel")
def adicionar_vacina_nao_perecivel(produto: VacinaNaoPerecivel):
    estoque.adicionar_produto(produto)
    return {"mensagem": "Vacina não perecível adicionada com sucesso!"}

@router.get("/", response_model=List[Union[ProdutoQuimioterapico, VacinaNaoPerecivel, VacinaPerecivel]])
def listar_todos():
    return estoque.listar_produtos()

@router.get("/pereciveis", response_model=List[VacinaPerecivel])
def listar_pereciveis():
    return estoque.listar_pereciveis()