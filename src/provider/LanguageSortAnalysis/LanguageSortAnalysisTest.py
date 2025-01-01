import unittest

from src.provider.LanguageSortAnalysis.LanguageSortAnalysis import LanguageSortAnalysis
import pandas as pd


class LanguageSortAnalysisTest(unittest.TestCase):

    def testNewInstance(self):
        instance = LanguageSortAnalysis()
        self.assertIsInstance(instance, LanguageSortAnalysis, "1. Devera ser instanciavel corretamente")

    def testAnalysis(self):
        instance = LanguageSortAnalysis()
        data = pd.read_csv("data/test.csv")
        response = instance.analysis(data)

        self.assertEqual(response.iloc[0,1], data.iloc[9,1], "2. 'analysis()' devera retornar valor valido caso possua parametros validos")

    def testAnalysisInvalidList(self):
        instance = LanguageSortAnalysis()
        value = bool(0)
        try:
            instance.analysis(0)
        except:
            value = bool(1)
            
        self.assertTrue(value, "3. 'analysis()' devera ser invalido caso o parametro seja invalido")

    def testAnalysisEmptyList(self):
        instance = LanguageSortAnalysis()
        value = bool(0)
        try:
            instance.analysis([])
        except:
            value = bool(1)
            
        self.assertTrue(value, "4. 'analysis()' devera ser invalido caso o parametro seja vazio")

if __name__ == '__main__':
    unittest.main()
