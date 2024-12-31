from model.TableAnalysis.TableAnalysis import TableAnalysis
from model.exception.InvalidParameterException.InvalidParameterException import InvalidParameterException
import pandas as pd
import numpy as np

# Classe para ordenacao quickSort
# @see TableAnalysis
class QuickSortAnalysis(TableAnalysis):

    # Realiza uma analise ordenacao quickSort
    # @param userInfoList Lista de dados a ser analisada
    # @returns Lista ordenada
    # @see TableAnalysis
    def analysis(self, userInfoList):
        if(not isinstance(userInfoList, pd.Series) or len(userInfoList) == 0):
            raise InvalidParameterException("'userInfoList' é None ou vazio")

        return self.__quickSort(userInfoList.values)

    # Iniciando quickSort
    # @param array Vetor a ser ordenado
    # @returns Vetor ordenado
    def __quickSort(self, array):
        # Limite da recursividade
        if len(array) <= 1:
            return array
        
        # Obtendo ponto central
        indexPivot = len(array) // 2
        pivotCredit = array[indexPivot].getCredit()
        menores = [value for value in array if value.getCredit() < pivotCredit]
        iguais = [value for value in array if value.getCredit() == pivotCredit]
        maiores = [value for value in array if value.getCredit() > pivotCredit]

        # Recursividade
        vetorMenor = self.__quickSort(menores)
        vetorMaior = self.__quickSort(maiores)

        # Resposta
        response = vetorMaior + iguais + vetorMenor
        return response
