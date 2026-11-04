# Projeto_DevOps

Markdown
# Projeto DevOps - Disciplina Integração DevOps

Aplicação desenvolvida para a disciplina de Integração DevOps. O projeto consiste em uma API REST desenvolvida em Python com **FastAPI**, persistência de dados em **SQLite** e uma interface web interativa.

---

##  Tecnologias Utilizadas

* **Linguagem:** Python 3.10
* **Framework Web:** FastAPI (com Jinja2 para a interface HTML)
* **Banco de Dados:** SQLite (via SQLAlchemy ORM)
* **Testes Automatizados:** Pytest & HTTPX
* **CI/CD Pipeline:** GitHub Actions

---

##  Como Executar o Projeto Localmente

### 1. Pré-requisitos
Certifique-se de ter o Python 3.10+ instalado em sua máquina.

### 2. Clonar o Repositório
```bash
git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
cd SEU-REPOSITORIO
3. Configurar o Ambiente Virtual
Windows:

PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1
Linux/Mac:

Bash
python -m venv venv
source venv/bin/activate
4. Instalar Dependências
Bash
pip install -r requirements.txt
5. Executar a Aplicação
Bash
uvicorn app.main:app --reload
Acesse no seu navegador:

Interface Web: http://127.0.0.1:8000

Documentação Swagger: http://127.0.0.1:8000/docs

 Como Executar os Testes Automatizados
Para rodar a suíte de testes do Pytest localmente:

Bash
pytest
 Pipeline de Integração Contínua (CI)
O projeto possui uma pipeline automatizada no GitHub Actions (.github/workflows/ci.yml) que é disparada a cada Push ou Pull Request na branch main. A pipeline realiza as seguintes etapas:

Checkout do código-fonte.

Configuração do ambiente Python.

Instalação automatizada das dependências.

Execução dos testes unitários e de integração com o pytest.

Versão 1.1.1

## Docker

Imagem multi-stage (`python:3.10-slim`), usuário não-root e healthcheck em `/health`.

    docker build -t projeto_devops .

## Docker Compose

    copy .env.example .env
    docker compose up --build

O banco SQLite fica no volume `db_data`, então os dados sobrevivem ao reinício do container.

## CD (GitHub Actions)

Ao enviar uma tag `vX.Y.Z`, o workflow `cd.yml` roda os testes, publica a imagem no GHCR (`ghcr.io/joao-299/projeto_devops`) e faz o deploy simulado em staging.

## Segredos e variáveis

- `DATABASE_URL`: secret do Environment `staging`.
- `SIMULATE_FAILURE`: variável do repositório (`true` provoca falha de propósito).
- `.env` fica fora do Git; `.env.example` mostra as variáveis necessárias.

## Versionamento e rollback

Versionamento semântico (`v1.0.0`, `v1.1.0`, `v1.1.1`). Se o deploy falhar, a pipeline volta sozinha para a versão estável anterior. Detalhes e prints em [docs/ROLLBACK.md](docs/ROLLBACK.md).