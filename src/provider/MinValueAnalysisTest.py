import unittest

from src.model.Table import Table
from src.provider.MinValueAnalysis import MinValueAnalysis

class MinValueAnalysisTest(unittest.TestCase):

    def testNewInstance(self):
        instance = MinValueAnalysis()
        self.assertIsInstance(instance, MinValueAnalysis, "1. Devera ser instanciavel corretamente")

    def testAnalysis(self):
        table = Table("./data/test.csv")
        instance = MinValueAnalysis()
        value = instance.analysis(table.getUserInfoList())            
        self.assertEqual(value, 1, "2. 'analysis()' devera ser valido caso possua parametros validos")

if __name__ == '__main__':
    unittest.main()