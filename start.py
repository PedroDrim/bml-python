from model.UserInfo.UserInfo import UserInfo
from src.provider.TableReader import TableReader
from src.provider.BenchmarkMeasure import BenchmarkMeasure
from src.provider.SummaryAnalysis import SummaryAnalysis
from src.provider.MergeSortAnalysis import MergeSortAnalysis
from src.provider.QuickSortAnalysis import QuickSortAnalysis
from src.provider.LanguageSortAnalysis import LanguageSortAnalysis
from model.TimeFormat.TimeFormat import TimeFormat
import numpy as np
import json
import sys

class Start:

    # Construtor publico da classe
    # @param configFile Arquivo de configuracao
    def __init__(self, configFile):

        # Obtendo configuracoes
        properties = self.__getConfig(configFile)
        bInput = properties["INPUT_FILENAME_LIST"]
        bOutput = properties["OUTPUT_FILENAME"]

        # Instanciando benchmark
        benchmark = BenchmarkMeasure()

        # Instanciando analises
        summaryAnalysis = SummaryAnalysis()
        mergeSortAnalysis = MergeSortAnalysis()
        quickSortAnalysis = QuickSortAnalysis()
        languageSortAnalysis = LanguageSortAnalysis()

        # Iterando os arquivos de dados
        for index in np.arange(len(bInput)):
            fileName = bInput[index]
            print("[START] Arquivo: " + str(index))

            #==================================================
            # Leitura dos dados
            print("\t[LOG] Read")
            benchmark.startState("Read@" + str(index))
            tableReader = TableReader(fileName)
            bList = tableReader.readAll()
            benchmark.endState("Read@" + str(index))
            #==================================================
            # Analise dos dados (Summary)
            print("\t[LOG] Summary")
            benchmark.startState("SummaryAnalysis@" + str(index))
            summary = summaryAnalysis.analysis(bList)
            benchmark.endState("SummaryAnalysis@" + str(index))
            #==================================================
            # Analise dos dados (Language)
            print("\t[LOG] Language")
            benchmark.startState("LanguageAnalysis@" + str(index))
            lang = languageSortAnalysis.analysis(bList)
            benchmark.endState("LanguageAnalysis@" + str(index))
            #==================================================
            # Convertendo de DataFrame para UserInfo[]
            bList = bList.apply(self.__asUserInfo, axis = 1)
            #==================================================
            # Analise dos dados (merge)
            print("\t[LOG] Merge")
            benchmark.startState("MergeAnalysis@" + str(index))
            merge = mergeSortAnalysis.analysis(bList)
            benchmark.endState("MergeAnalysis@" + str(index))
            #==================================================
            # Analise dos dados (Quick)
            print("\t[LOG] Quick")
            benchmark.startState("QuickAnalysis@" + str(index))
            quick =  quickSortAnalysis.analysis(bList)
            benchmark.endState("QuickAnalysis@" + str(index))
            #==================================================

            print("[END] Arquivo: " + str(index))

        # Exportando resultado
        benchmark.export(bOutput, TimeFormat.MILLISEGUNDOS)

    def __asUserInfo(self, pdTableRow):
        userInfo = UserInfo(pdTableRow.iloc[0], pdTableRow.iloc[1], pdTableRow.iloc[2])
        return userInfo

    # Metodo responsavel por ler o arquivo de configuracao
    # @param fileName Arquivo de configuracao
    # @returns Dados de configuracao
    def __getConfig(self, fileName):
        f = open(fileName, 'r')
        serializedJson = f.read()
        f.close()

        obj = json.loads(serializedJson)
        return obj

Start(sys.argv[1])
