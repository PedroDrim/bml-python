# Buil alpine
FROM alpine:3.14 AS build

# Create build directory
WORKDIR /build

# Copy files to directory
COPY ./data /build/

# Descompando arquivos de simulacao
RUN unzip simulationInput_M.zip -d .

FROM python:3.14-rc-slim

# Create app directory
WORKDIR /app

# Copy files to directory
COPY ./ /app/

# Instalando gcc
RUN apt update && apt install -y build-essential unzip

# Instalando pacotes
RUN pip install -r requirements.txt

# Executando testes
RUN coverage run --source=src -m unittest discover -s src -p "*Test.py"

# Copiando tudo para deploy
COPY --from=build ./build /app/data

# Iniciando CLI
ENTRYPOINT ["sh","Bench.sh"]
