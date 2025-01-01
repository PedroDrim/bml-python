from src.model.TableAnalysis.TableAnalysis import TableAnalysis
from src.model.exception.InvalidParameterException.InvalidParameterException import InvalidParameterException
import pandas as pd

# Classe para ordenacao mergeSort
# @see model.TableAnalysis
class MergeSortAnalysis(TableAnalysis):

    # Realiza uma ordenacao mergeSort
    # @param userInfoList Lista de dados a ser analisada
    # @returns Lista ordenada
    # @see TableAnalysis
    def analysis(self, userInfoList):
        if(not isinstance(userInfoList, pd.Series) or len(userInfoList) == 0):
            raise InvalidParameterException("'userInfoList' é invalido ou vazio")
        
        return self.__mergeSort(userInfoList.values)

    # Iniciando mergeSort 
    # @param array Vetor a ser ordenado
    # @returns Vetor ordenado
    def __mergeSort(self, array):
        if len(array) <= 1:
            return array

        # Obtendo posicao central
        meio = len(array) // 2

        # Separando vetores
        vetorEsquerda = array[:meio]
        vetorDireita = array[meio:]

        # Aplicando recursividade
        esquerda = self.__mergeSort(vetorEsquerda)
        direita = self.__mergeSort(vetorDireita)

        # Unificando vetores da esquerda, meio e direita
        return self.__merge(esquerda, direita)

    # Metodo responsavel por comparar e unificar os vetores
    # @param esquerda Vetor da esquerda
    # @param direita vetor da direita
    # @returns Vetor ordenado
    def __merge(self, esquerda, direita):
        # Iniciando vetor vazio
        resultado = []

        while len(esquerda) > 0 and len(direita) > 0:
            # Comparando valores
            if esquerda[0].getCredit() > direita[0].getCredit():
                # .pop(0)
                resultado.append(esquerda[0])
                esquerda = esquerda[1:]
            else:
                # .pop(0)
                resultado.append(direita[0])
                direita = direita[1:]

        # Aplicando resto dos vetores
        resultado.extend(esquerda)
        resultado.extend(direita)

        # Retornando vetor ordenado
        return resultado