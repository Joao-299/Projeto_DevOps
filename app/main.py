from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import List
from pydantic import BaseModel

# -------------------------------------------------------------------
# 1. Configuração do Banco de Dados (SQLite)
# -------------------------------------------------------------------
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelo de Tabela no Banco
class ItemModel(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    completed = Column(Boolean, default=False)

# Cria as tabelas automaticamente
Base.metadata.create_all(bind=engine)

# Dependency para obter a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------------------------------------------------------
# 2. Schemas Pydantic (Validação de Dados)
# -------------------------------------------------------------------
class ItemCreate(BaseModel):
    title: str

class ItemResponse(BaseModel):
    id: int
    title: str
    completed: bool

    class Config:
        from_attributes = True

# -------------------------------------------------------------------
# 3. Aplicação FastAPI e Endpoints
# -------------------------------------------------------------------
app = FastAPI(
    title="Projeto DevOps - API e Interface",
    description="Aplicação com banco de dados SQLite e interface Web interativa.",
    version="1.0.0"
)

# Rota Básica / Healthcheck
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# --- Endpoints da API REST ---

@app.post("/api/items", response_model=ItemResponse, status_code=201)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = ItemModel(title=item.title)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/api/items", response_model=List[ItemResponse])
def read_items(db: Session = Depends(get_db)):
    return db.query(ItemModel).all()

# --- Interface Web (HTML Simples) ---

@app.get("/", response_class=HTMLResponse)
def home_page():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Projeto DevOps</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f9; }
            h1 { color: #333; }
            .card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); max-width: 500px; }
            a { color: #0066cc; text-decoration: none; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Projeto DevOps - Integração CI/CD</h1>
            <p>Sua aplicação com banco de dados SQLite está rodando com sucesso!</p>
            <p>Acesse a <strong>Interface de Testes/Documentação (Swagger):</strong></p>
            <a href="/docs" target="_blank">👉 Abrir Interface Interativa (/docs)</a>
        </div>
    </body>
    </html>
    """
