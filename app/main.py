from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import HTMLResponse
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

class ItemModel(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    completed = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------------------------------------------------------
# 2. Schemas Pydantic
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
app = FastAPI(title="Projeto DevOps - Interface Completa")

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

# NOVO ENDPOINT: Deletar item pelo ID
@app.delete("/api/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    
    db.delete(db_item)
    db.commit()
    return None

# --- Interface Web Visual Completa (Frontend Integrado) ---

@app.get("/", response_class=HTMLResponse)
def home_page():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Painel de Controle - DevOps</title>
        <style>
            * { box-sizing: border-box; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
            body { background-color: #f0f2f5; margin: 0; padding: 40px 20px; display: flex; justify-content: center; }
            .container { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); width: 100%; max-width: 500px; }
            h1 { color: #1a73e8; font-size: 24px; margin-bottom: 8px; text-align: center; }
            p.subtitle { color: #5f6368; text-align: center; font-size: 14px; margin-bottom: 24px; }
            .form-group { display: flex; gap: 10px; margin-bottom: 20px; }
            input[type="text"] { flex: 1; padding: 12px; border: 1px solid #dadce0; border-radius: 6px; font-size: 14px; outline: none; }
            input[type="text"]:focus { border-color: #1a73e8; }
            button.btn-add { background: #1a73e8; color: white; border: none; padding: 12px 20px; border-radius: 6px; cursor: pointer; font-weight: bold; transition: background 0.2s; }
            button.btn-add:hover { background: #1557b0; }
            ul { list-style: none; padding: 0; margin: 0; }
            li { background: #f8f9fa; border: 1px solid #e8eaed; padding: 12px; border-radius: 6px; margin-bottom: 8px; display: flex; justify-content: space-between; align-items: center; font-size: 14px; }
            .item-actions { display: flex; align-items: center; gap: 8px; }
            .btn-delete { background: #dc3545; color: white; border: none; padding: 6px 10px; border-radius: 4px; cursor: pointer; font-size: 12px; font-weight: bold; transition: background 0.2s; }
            .btn-delete:hover { background: #bd2130; }
            .footer-link { text-align: center; margin-top: 20px; font-size: 13px; }
            .footer-link a { color: #1a73e8; text-decoration: none; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Projeto DevOps</h1>
            <p class="subtitle">Gerenciador de Tarefas Integrado ao SQLite</p>
            
            <form id="itemForm" class="form-group">
                <input type="text" id="itemTitle" placeholder="Digite uma nova tarefa..." required>
                <button type="submit" class="btn-add">Adicionar</button>
            </form>

            <ul id="itemsList"></ul>

            <div class="footer-link">
                <a href="/docs" target="_blank">Documentação Swagger da API ➔</a>
            </div>
        </div>

        <script>
            const API_URL = '/api/items';

            async function loadItems() {
                const res = await fetch(API_URL);
                const items = await res.json();
                const list = document.getElementById('itemsList');
                list.innerHTML = '';
                items.forEach(item => {
                    const li = document.createElement('li');
                    li.innerHTML = `
                        <span>${item.title}</span>
                        <div class="item-actions">
                            <button class="btn-delete" onclick="deleteItem(${item.id})">Apagar</button>
                        </div>
                    `;
                    list.appendChild(li);
                });
            }

            document.getElementById('itemForm').addEventListener('submit', async (e) => {
                e.preventDefault();
                const input = document.getElementById('itemTitle');
                const title = input.value;
                
                await fetch(API_URL, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ title })
                });

                input.value = '';
                loadItems();
            });

            async function deleteItem(id) {
                await fetch(`${API_URL}/${id}`, {
                    method: 'DELETE'
                });
                loadItems();
            }

            loadItems();
        </script>
    </body>
    </html>
    """
