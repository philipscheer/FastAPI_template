# Usar uma imagem base do Python
FROM python:3.10-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos de dependências
COPY requirements.txt .

# Atualizar o pip para evitar problemas de compatibilidade
RUN pip install --upgrade pip

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código para o container
COPY . .

# Expor a porta que a aplicação usará
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
