import unittest

from src.model.TableAnalysis.TableAnalysis import TableAnalysis

class MockTableAnalysis(TableAnalysis):
    def analysis(self, userInfoList):
        return 0

class TableAnalysisTest(unittest.TestCase):

    def testIntegration(self):
        instance = MockTableAnalysis()

        value = bool(0)
        try:
            instance.analysis([])
        except:
            value = bool(1)
            
        self.assertFalse(value, "1. Integracao com 'TableAnalysis'")

if __name__ == '__main__':
    unittest.main()
