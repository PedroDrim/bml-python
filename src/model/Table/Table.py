import pandas as pd

# Classe para gerenciar uma tabela de usuarios
class Table:

    # Construtor publico da classe
    # @param fileName Nome do arquivo .csv
    def __init__(self, fileName):
        self.__fileName = fileName
        self.__userInfoList = self.__deserializeFile(self.__fileName)

    # Metodo publico para obter o nome do arquivo
    # @returns Nome do arquivo
    def getFileName(self):
        return self.__fileName

    # Metodo publico para obter a lista de usuarios
    # @returns Lista de usuarios
    def getUserInfoList(self):
        return self.__userInfoList

    # Método privado para conversão do arquivo .csv em uma lista de usuarios
    # @param fileName Nome do arquivo
    # @returns Tabela pandas de usuarios    
    def __deserializeFile(self, fileName):
        table = pd.read_csv(fileName)
        return table
