import unittest

from src.model.Table.Table import Table
from src.provider.MeanAnalysis.MeanAnalysis import MeanAnalysis

class MeanAnalysisTest(unittest.TestCase):

    def testNewInstance(self):
        instance = MeanAnalysis()
        self.assertIsInstance(instance, MeanAnalysis, "1. Devera ser instanciavel corretamente")

    def testAnalysis(self):
        table = Table("./data/test.csv")
        instance = MeanAnalysis()
        value = instance.analysis(table.getUserInfoList())            
        self.assertEqual(value, 5.5, "2. 'analysis()' devera ser valido caso possua parametros validos")

if __name__ == '__main__':
    unittest.main()