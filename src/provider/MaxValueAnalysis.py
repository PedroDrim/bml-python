from src.model.SimpleTableAnalysis import SimpleTableAnalysis
from src.model.UserInfo import UserInfo

# Classe de analise que implementa a interface "SimpleTableAnalysis"
class MaxValueAnalysis(SimpleTableAnalysis):

    # Método responsável por obter o maior valor de credit na lista de usuarios
    # @param userInfoList Lista de usuarios
    # @returns Valor máximo da lista
    def analysis(self, userInfoList):
        vmax = userInfoList["credit"].max()
        return vmax