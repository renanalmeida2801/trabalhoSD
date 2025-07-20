from fastapi import FastAPI
from app.routers import produtos, estoque

app = FastAPI(title="API de Produtos Veterinários")

app.include_router(produtos.router)
app.include_router(estoque.router)