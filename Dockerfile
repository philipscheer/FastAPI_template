# Usar uma imagem base do Python
FROM python:3.10-slim

# Definir o diret�rio de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos de depend�ncias
COPY requirements.txt .

# Atualizar o pip para evitar problemas de compatibilidade
RUN pip install --upgrade pip

# Instalar as depend�ncias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do c�digo para o container
COPY . .

# Expor a porta que a aplica��o usar�
EXPOSE 8000

# Comando para iniciar a aplica��o
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
