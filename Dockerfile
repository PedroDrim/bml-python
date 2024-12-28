FROM python:3.14-rc-slim

# Create app directory
WORKDIR /app

# Copy files to directory
COPY ./ /app/

# Instalando gcc
RUN apt update && apt install -y build-essential

# Instalando pacotes
RUN pip install numpy

# Executando testes
RUN sh Test.sh

# Iniciando CLI
ENTRYPOINT ["sh","Bench.sh"]