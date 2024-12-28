FROM python:3.14-rc-slim

# Create app directory
WORKDIR /app

# Copy files to directory
COPY ./ /app/

# Instalando gcc
RUN apt update && apt install -y build-essential unzip

# Instalando pacotes
RUN pip install pandas

# Executando testes
RUN sh Test.sh

# Descompando arquivos de simulacao
RUN unzip data/simulationInput.zip -d data

# Iniciando CLI
ENTRYPOINT ["sh","Bench.sh"]