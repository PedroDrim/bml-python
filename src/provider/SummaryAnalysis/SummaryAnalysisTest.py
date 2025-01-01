import unittest

from src.provider.SummaryAnalysis.SummaryAnalysis import SummaryAnalysis
import pandas as pd


class SummaryAnalysisTest(unittest.TestCase):

    def testNewInstance(self):
        instance = SummaryAnalysis()
        self.assertIsInstance(instance, SummaryAnalysis, "1. Devera ser instanciavel corretamente")

    def testAnalysis(self):
        instance = SummaryAnalysis()
        data = pd.read_csv("data/test.csv")
        response = instance.analysis(data)

        self.assertListEqual(response, [1, 10, 5.5], "2. 'analysis()' devera retornar valor valido caso possua parametros validos")

    def testAnalysisInvalidList(self):
        instance = SummaryAnalysis()
        value = bool(0)
        try:
            instance.analysis(0)
        except:
            value = bool(1)
            
        self.assertTrue(value, "3. 'analysis()' devera ser invalido caso o parametro seja invalido")

    def testAnalysisEmptyList(self):
        instance = SummaryAnalysis()
        value = bool(0)
        try:
            instance.analysis([])
        except:
            value = bool(1)
            
        self.assertTrue(value, "4. 'analysis()' devera ser invalido caso o parametro seja vazio")

if __name__ == '__main__':
    unittest.main()
