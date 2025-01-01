from src.model.BenchmarkOutput.BenchmarkOutput import BenchmarkOutput
from src.model.exception.InvalidParameterException.InvalidParameterException import InvalidParameterException
from src.model.exception.DataReaderException.DataReaderException import DataReaderException
from src.model.exception.BenchmarkException.BenchmarkException import BenchmarkException
from src.model.TimeFormat.TimeFormat import TimeFormat

import time
import json

# Classe para captura de estados de tempo
# @see model.BenchmarkOutput
class BenchmarkMeasure(BenchmarkOutput):

    # Construtor publico da classe
    def __init__(self):
        self.__benchMap = {}
        self.__START_MARK = "_S"
        self.__END_MARK = "_E"

    # Inicio da captura de estado
    # @param tag Nome da captura referente
    def startState(self, tag):
        if(not isinstance(tag, str)):
            raise InvalidParameterException("'tag' e invalido")

        bTime = time.time()
        sym = tag + self.__START_MARK
        self.__benchMap[sym] = bTime

    # Fim da captura de estado
    # @param tag Nome da captura referente
    def endState(self, tag):
        if(not isinstance(tag, str)):
            raise InvalidParameterException("'tag' e invalido")

        bTime = time.time()
        sym = tag + self.__END_MARK
        self.__benchMap[sym] = bTime
    
    # Resultado da captura de estado especifica
    # @param tag Nome da captura referente
    # @param format Formato do resultado
    # @return Tempo decorrido entre o inicio e o fim da captura de estado
    def resultByTag(self, tag, format):
        if(not isinstance(tag, str)):
            raise InvalidParameterException("'tag' e invalido")

        if(not isinstance(format, TimeFormat)):
            raise InvalidParameterException("'format' e invalido")

        startSym = tag + self.__START_MARK
        endSym = tag + self.__END_MARK

        startTag = startSym in self.__benchMap
        endTag = endSym in self.__benchMap

        if(not startTag or not endTag):
            raise BenchmarkException("Não encontrado par 'inicio-fim' de:" + tag)

        startTime = self.__benchMap[startSym]
        endTime = self.__benchMap[endSym]
        
        return (endTime - startTime) * format.value
    
    # Resultado de todas as capturas de estado
    # @param format Formato do resultado
    # @return Mapa contendo o tempo decorrido entre o inicio e o fim da captura de estado para cada estado gerado.
    def result(self, format):
        if(not isinstance(format, TimeFormat)):
            raise InvalidParameterException("'format' e invalido")

        mapResult = {}

        for key in self.__benchMap:
            tag = key.split("_")[0]
            time = self.resultByTag(tag, format)
            mapResult[tag] = time

        return mapResult

    # Exporta o resultado no formato de um arquivo
    # @param fileName Nome do arquivo de saida
    # @param format Formato do resultado
    def export(self, fileName, format):
        if(not isinstance(fileName, str)):
            raise InvalidParameterException("'tag' e invalido")
        
        if(not isinstance(format, TimeFormat)):
            raise InvalidParameterException("'format' e invalido")

        mapResult = self.result(format)
        serilizedString = json.dumps(mapResult)
        
        try:
            f = open(fileName, 'w')
            f.write(serilizedString)
            f.close()
        except:
            raise DataReaderException("Arquivo não encontrado:" + fileName)
