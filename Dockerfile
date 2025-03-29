FROM python:3.14-rc-slim

# Create app directory
WORKDIR /app

# Copy files to directory
COPY ./ /app/

# Instalando gcc
RUN apt update && apt install -y build-essential unzip

# Instalando pacotes
RUN pip install pandas numpy coverage

# Executando testes
RUN coverage run --source=src -m unittest discover -s src -p "*Test.py"

# Descompando arquivos de simulacao
RUN unzip data/simulationInput_M.zip -d data

# Iniciando CLI
ENTRYPOINT ["sh", "Bench.sh"]
