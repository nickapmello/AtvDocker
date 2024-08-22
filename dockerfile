# Dockerfile
FROM python:3.8-slim

# Definir o diretório de trabalho
WORKDIR /app

# Instalar as dependências
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copiar o aplicativo Flask
COPY . /app/

# Expor a porta em que o Flask será executado
EXPOSE 5000

# Comando para rodar o aplicativo
CMD ["python", "app.py"]
