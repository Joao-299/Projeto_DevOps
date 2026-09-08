# Projeto Integrador — Gerenciador de Tarefas

Projeto desenvolvido para demonstrar:

- Código-fonte funcional;
- Interface web para interação;
- Banco de dados SQLite;
- Testes automatizados;
- Integração Contínua com GitHub Actions;
- Containerização com Docker.

## Tecnologias

Python 3.12, Flask, SQLite, Pytest e Docker.

## Como executar localmente

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
python -m app.app
```

Acesse: http://localhost:5000

## Como executar os testes

```bash
pytest -v
```

## Como executar com Docker

```bash
docker compose up --build
```

Acesse: http://localhost:5000

## Estratégia Git

Foi adotada a estratégia Trunk-Based Development:

- `main`: branch principal e estável;
- branches curtas para tarefas: `feature/nome-da-tarefa`;
- Pull Requests obrigatórios antes do merge;
- revisão de código por outro integrante;
- pipeline de CI executada a cada Push e Pull Request;
- commits padronizados, por exemplo:
  - `feat: adiciona cadastro de tarefas`
  - `test: cria testes da API`
  - `fix: valida título vazio`
  - `docs: atualiza README`

## Divisão sugerida do grupo

- Desenvolvedor: implementação da aplicação e banco de dados;
- Qualidade: testes automatizados e validações;
- Operações/Infraestrutura: Docker, GitHub Actions e organização do repositório.

## Entregas atendidas

1. Repositório estruturado com estratégia de ramificação;
2. Aplicação funcional com interface e persistência;
3. Suite de testes unitários e de integração;
4. Pipeline de CI;
5. Dockerfile e Docker Compose.
