import unittest

from src.model.Table.Table import Table
from src.provider.MaxValueAnalysis.MaxValueAnalysis import MaxValueAnalysis

class MaxValueAnalysisTest(unittest.TestCase):

    def testNewInstance(self):
        instance = MaxValueAnalysis()
        self.assertIsInstance(instance, MaxValueAnalysis, "1. Devera ser instanciavel corretamente")

    def testAnalysis(self):
        table = Table("./data/test.csv")
        instance = MaxValueAnalysis()
        value = instance.analysis(table.getUserInfoList())            
        self.assertEqual(value, 10, "2. 'analysis()' devera ser valido caso possua parametros validos")

if __name__ == '__main__':
    unittest.main()