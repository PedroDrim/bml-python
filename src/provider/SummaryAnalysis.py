from model.TableAnalysis.TableAnalysis import TableAnalysis
from model.exception.InvalidParameterException.InvalidParameterException import InvalidParameterException
import pandas as pd

# Classe para analise de dados, obtem os valores maximo e minimo dos creditos dos usuarios
# @see model.TableAnalysis
class SummaryAnalysis(TableAnalysis): 
    
    # Realiza a analise maxima e minima dos dados
    # @param userInfoList Lista de dados a ser analisada
    # @returns Valores maximo e minimo dos creditos
    # @see TableAnalysis
    def analysis(self, userInfoList):
        if(not isinstance(userInfoList, pd.DataFrame) or userInfoList.empty):
            raise InvalidParameterException("'userInfoList' e invalido")

        vmax = userInfoList["credit"].max()
        vmin = userInfoList["credit"].min()
        vmean = userInfoList["credit"].mean()
        return [vmin, vmax, vmean]

