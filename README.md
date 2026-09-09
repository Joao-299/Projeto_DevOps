# Projeto_DevOps

Markdown
# Projeto DevOps - API Flask com CI/CD

[![CI Pipeline](https://github.com/Joao-299/Projeto_DevOps/actions/workflows/ci.yml/badge.svg)](https://github.com/Joao-299/Projeto_DevOps/actions/workflows/ci.yml)

Este repositório contém a entrega do projeto prático de DevOps. O objetivo principal do projeto é demonstrar a integração entre o desenvolvimento de uma aplicação web simples, a criação de testes unitários e a implementação de uma esteira de Integração Contínua (CI) automatizada.

## 🛠️ Tecnologias Utilizadas

*   **Python 3.9:** Linguagem principal do projeto.
*   **Flask:** Micro-framework utilizado para a construção da API REST.
*   **Pytest:** Framework utilizado para a estruturação e execução dos testes unitários.
*   **GitHub Actions:** Plataforma de CI/CD utilizada para automatizar a validação do código.

## 📂 Estrutura do Repositório

O projeto foi organizado com a seguinte estrutura de diretórios:

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml         # Configuração da esteira de Integração Contínua
├── app/
│   └── main.py            # Código-fonte da API Flask
└── tests/
    └── test_app.py        # Testes unitários da aplicação
🚀 Como Executar o Projeto Localmente
1. Clonar o repositório
Bash
git clone [https://github.com/Joao-299/Projeto_DevOps.git](https://github.com/Joao-299/Projeto_DevOps.git)
cd Projeto_DevOps
2. Instalar as dependências
Certifique-se de ter o Python instalado e execute:

Bash
pip install flask pytest
3. Iniciar a API
Bash
python app/main.py
A API estará disponível no endereço http://localhost:5000/. Ao acessar a rota raiz (/), você receberá a seguinte resposta em formato JSON:

JSON
{
  "message": "API DevOps funcionando!"
}
🧪 Como Executar os Testes
Para garantir que a aplicação está funcionando conforme o esperado, o projeto conta com testes automatizados. Para rodá-los localmente, utilize o comando:

Bash
python -m pytest tests/
⚙️ Integração Contínua (CI)
Este projeto utiliza o GitHub Actions para garantir a qualidade contínua do código. A esteira foi configurada no arquivo ci.yml e é acionada automaticamente sempre que há um push ou pull_request para a branch main.

O pipeline realiza os seguintes passos:

Provisiona uma máquina virtual com Ubuntu (ubuntu-latest).

Faz o checkout do código do repositório.

Configura o ambiente com o Python 3.9.

Instala as dependências necessárias (flask e pytest).

Executa a suíte de testes automaticamente com o comando python -m pytest tests/.
