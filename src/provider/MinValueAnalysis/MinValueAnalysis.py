from src.model.SimpleTableAnalysis.SimpleTableAnalysis import SimpleTableAnalysis

# Classe de analise que implementa a interface "SimpleTableAnalysis"
class MinValueAnalysis(SimpleTableAnalysis):

    # Método responsável por obter o menor valor de credit na lista de usuarios
    # @param userInfoList Lista de usuarios
    # @returns Valor minimo da lista
    def analysis(self, userInfoList):
        vmin = userInfoList["credit"].min()
        return vmin
