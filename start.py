
import sys
import time
import numpy as np

from src.model.UserInfo import UserInfo

# Classe inicial do sistema
class Start:

    # Método de inicialização do projeto
    # @param args Lista de parametros obtidos via console
    def __init__(self, param):
        # Obtendo tamanho da lista
        tamanho = self.__getParam(param)
        antes = time.time()

        userList = np.arange(tamanho)
        userList = map(self.__createUserInfo, userList)
        
        # Abrindo resposta do map (Isso carrega o objeto inteiro na memoria e permite acesso)
        userList = list(userList)

        response = (time.time() - antes) * 1000.0

        print("[START] Typescript_" + str(tamanho))
        print("[OK]Tamanho: " + str(tamanho))
        print("[OK]Tempo: " + str(response) + " ms")
        print("[END] Typescript_" + str(tamanho))

    # Metodo responsavel por criar um usuario
    # @param index Identificador do usuario
    # @returns Novo usuario
    def __createUserInfo(self, index):
        sIndex = str(index)
        user = "user%s" % sIndex
        password = "password%s" % sIndex
        return UserInfo(user, password)

    # Método para captura e tratamento dos parametros obtidos via console
    # @param codes Lista de parametros obtidos via console
    # @return Tamanho de usuários á serem gerados
    def __getParam(self, codes):
        if(len(codes) != 2):
            print("Parametros inválidos.")
            sys.exit(-1)
            
        line = int(codes[1])

        if(line <= 0):
            print("Quantidade de linhas menor que 1.")
            sys.exit(-1)
       
        return line        

Start(sys.argv)
