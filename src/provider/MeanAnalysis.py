from src.model.SimpleTableAnalysis import SimpleTableAnalysis
from src.model.UserInfo import UserInfo

# Classe de analise que implementa a interface "SimpleTableAnalysis"
class MeanAnalysis(SimpleTableAnalysis):

    # Método responsável por obter a media de valores de credit na lista de usuarios
    # @param userInfoList Lista de usuarios
    # @returns Média de valores da lista
    def analysis(self, userInfoList):
        vmean = userInfoList["credit"].mean()
        return vmean
