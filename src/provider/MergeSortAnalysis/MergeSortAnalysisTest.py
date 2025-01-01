import unittest

from src.model.UserInfo.UserInfo import UserInfo
from src.provider.MergeSortAnalysis.MergeSortAnalysis import MergeSortAnalysis

import pandas as pd


class MergeSortAnalysisTest(unittest.TestCase):

    def testNewInstance(self):
        instance = MergeSortAnalysis()
        self.assertIsInstance(instance, MergeSortAnalysis, "1. Devera ser instanciavel corretamente")

    def testAnalysis(self):
        instance = MergeSortAnalysis()
        data = pd.Series([UserInfo("u1", "p1", 1), UserInfo("u2", "p2", 2), UserInfo("u3", "p3", 3)])
        response = instance.analysis(data)

        self.assertEqual(response[0], data[len(data) - 1], "2. 'analysis()' devera retornar valor valido caso possua parametros validos")

    def testAnalysisInvalidList(self):
        instance = MergeSortAnalysis()
        value = bool(0)
        try:
            instance.analysis(0)
        except:
            value = bool(1)
            
        self.assertTrue(value, "3. 'analysis()' devera ser invalido caso o parametro seja invalido")

    def testAnalysisEmptyList(self):
        instance = MergeSortAnalysis()
        value = bool(0)
        try:
            instance.analysis([])
        except:
            value = bool(1)
            
        self.assertTrue(value, "4. 'analysis()' devera ser invalido caso o parametro seja vazio")

if __name__ == '__main__':
    unittest.main()
