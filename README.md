# bml-Python

[![Docker Build](https://github.com/PedroDrim/bml-python/actions/workflows/python.yml/badge.svg?branch=inputclass)](https://github.com/PedroDrim/bml-python/actions)
[![CodeQL Security](https://github.com/PedroDrim/bml-python/actions/workflows/codeql.yml/badge.svg?branch=inputclass)](https://github.com/PedroDrim/bml-python/actions)
[![Codacy](https://github.com/PedroDrim/bml-python/actions/workflows/codacy.yml/badge.svg?branch=inputclass)](https://github.com/PedroDrim/bml-python/actions)

### Introdução

O objetivo deste repositório é estudar o comportamento, estrutura e o desempenho da linguagem typescript.

Este repositório funciona como um plugin para o repositório princial **Benchmark Languages**.

Ferramentas utilizadas neste repositório bem como suas versões:

|Ferramenta |Versão  |
|-----------|--------|
|Python3    |3.13.1  |
|Docker     |24.0.7  |

### Instalação

1. Clone este repositório com o comando abaixo, onde **\<branch\>** se refere ao experimento que deseja realizar:

```
git clone -b <branch> https://github.com/PedroDrim/bml-python
```

2. Instale o [**Docker**](https://docs.docker.com/engine/install/).

3. Entre no diretório do repositório clonado e execute o **Docker** para iniciar as simulaçoes:

```
# Gerando build docker
sudo docker build -t inputclass_python .

# Executando container
sudo docker run inputclass_python
```

4. O resultado sairá no STDOUT no seguinte formato:

```
[START] Python_data/data_1e+06.csv
[OK]Arquivo: data/data_1e+06.csv
[OK]Tempo_leitura: 600.3546714782715 ms
[OK]Tempo_analise: 1.7704963684082031 ms
[OK]Max: 1000000
[OK]Min: 1
[OK]Mean: 500000.5
[END] Python_data/data_1e+06.csv
```

### Garantia de Qualidade

Este é um pequeno checklist para que eu garanta que a simulação irá funcionar seguindo os seguintes critérios de qualidade:

- [x] Possui teste automatizado?
- [x] Os testes automatizados funcionam corretamente?
- [x] Possui arquivo de simulação (Bench.sh)?
- [x] O arquivo de simulação (Bench.sh) funciona corretamente?
- [x] Possui **Dockerfile**?
- [x] O arquivo **Dockerfile** funciona corretamente?
- [x] O repositório possui um passo-a-passo de como executar a simulação?
- [x] Esta simulação está contida em um branch individual?
- [x] Esta simulação possui um **release**?

### Experimentos

Esta seção é a mais divertida (na minha opinião), pois nela descrevo os experimentos realizados com as linguagens bem como as técnicas utilizadas para as respectivas análises.

| Nome (com link) | Objetivo | Técnicas utilizadas para análise |
|-----------------|----------|----------------------------------|
| [simpleclass](https://github.com/PedroDrim/Benchmark-Languages/blob/simpleclass/Documents/simpleclass.md) | Estudar a criação de classes simples | Scatterplot de média com desvio padrão e regressão linear simples.|
