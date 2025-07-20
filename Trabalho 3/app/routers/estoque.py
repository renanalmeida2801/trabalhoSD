from fastapi import APIRouter
from app.database import estoque

router = APIRouter(prefix="/estoque", tags=["Estoque"])

@router.get("/quantidade_total")
def quantidade_total():
    return {"total_produtos": len(estoque.listar_produtos(  ))}