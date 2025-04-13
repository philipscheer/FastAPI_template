# Projeto FastAPI com Controle de Estoque Omnichannel

Este projeto é uma API desenvolvida com **FastAPI** para gerenciar usuários e produtos, incluindo controle de estoque, seguindo boas práticas de mercado. Ele foi projetado para ser escalável, modular e fácil de manter.

---

## Funcionalidades Principais

- **Gerenciamento de Usuários**: Cadastro, leitura, atualização e exclusão de usuários.
- **Gerenciamento de Produtos**: Cadastro, leitura, atualização e exclusão de produtos, com controle de estoque.
- **Controle de Estoque**: Cada produto possui um campo `stock` para rastrear a quantidade disponível.
- **Estrutura Modular**: Separação clara entre modelos, esquemas, endpoints e configuração.

---

## Boas Práticas Utilizadas

1. **Estrutura Modular**:
   - Os arquivos estão organizados em diretórios como `models`, `schemas`, `endpoints` e `db` para facilitar a manutenção e escalabilidade.

2. **SQLAlchemy para ORM**:
   - Utilizamos o SQLAlchemy para interagir com o banco de dados, garantindo flexibilidade e robustez.

3. **Pydantic para Validação**:
   - Os esquemas (schemas) utilizam o Pydantic para validação de dados de entrada e saída.

4. **Dependências no FastAPI**:
   - A função `get_db` é usada como dependência para gerenciar sessões de banco de dados de forma eficiente.

5. **Rotas Versionadas**:
   - As rotas estão organizadas por versões (ex.: `v1`) para facilitar futuras atualizações sem quebrar compatibilidade.

6. **Configuração Centralizada**:
   - As configurações do projeto estão centralizadas no arquivo `app/core/config.py`, permitindo fácil modificação.

---

## Como Adicionar Novos Endpoints

### Passo 1: Criar o Modelo
Adicione o modelo no diretório `app/models`. Por exemplo, para um novo recurso `Order`:

### Passo 2: Criar o Esquema
Adicione o esquema no diretório `app/schemas`. Exemplo para `Order`:

### Passo 3: Criar o Endpoint
Adicione o endpoint no diretório `app/api/v1/endpoints`. Exemplo para `Order`:

### Passo 4: Registrar o Endpoint
No arquivo `app/main.py`, registre o novo endpoint:

---

## Como Iniciar o Projeto

### Passo 1: Instalar Dependências
Certifique-se de que você tenha o Docker instalado.

### Passo 2: Construir e Iniciar os Contêineres
Certifique-se de que o Docker e o Docker Compose estão instalados em sua máquina. Para iniciar o projeto, execute os seguintes comandos no terminal:

1. **Construir os contêineres**:
docker-compose build

2. **Iniciar os contêineres**:
docker-compose up

### Passo 3: Acessar a Documentação
Após iniciar o servidor, você pode acessar a documentação interativa da API nos seguintes links:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Passo 4: Parar os Contêineres
Para parar os contêineres, utilize o comando:
docker-compose down

