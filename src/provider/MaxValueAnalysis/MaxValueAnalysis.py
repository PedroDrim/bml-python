from src.model.SimpleTableAnalysis.SimpleTableAnalysis import SimpleTableAnalysis

# Classe de analise que implementa a interface "SimpleTableAnalysis"
class MaxValueAnalysis(SimpleTableAnalysis):

    # Método responsável por obter o maior valor de credit na lista de usuarios
    # @param userInfoList Lista de usuarios
    # @returns Valor máximo da lista
    def analysis(self, userInfoList):
        vmax = userInfoList["credit"].max()
        return vmax