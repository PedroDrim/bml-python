from src.model.TableAnalysis import TableAnalysis
from src.model.exception.InvalidParameterException import InvalidParameterException
import pandas as pd

# Classe para analise de dados, obtem um usuario aleatoriamente
# @see TableAnalysis
class LanguageSortAnalysis(TableAnalysis):

    # Realiza uma analise aleatoria dos dados
    # @param userInfoList Lista de dados a ser analisada
    # @returns Elemento aleatorio da lista
    # @see TableAnalysis
    def analysis(self, userInfoList):
        if(not isinstance(userInfoList, pd.DataFrame) or userInfoList.empty):
            raise InvalidParameterException("'userInfoList' é None ou vazio")

        sortedList = userInfoList.sort_values(by=['credit'])
        return sortedList