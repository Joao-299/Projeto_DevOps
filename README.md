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
