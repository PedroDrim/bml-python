import unittest

from src.model.SimpleTableAnalysis import SimpleTableAnalysis

class MockSimpleTableAnalysis(SimpleTableAnalysis):
    def analysis(self, userInfoList):
        return 0

class SimpleTableAnalysisTest(unittest.TestCase):

    def testIntegration(self):
        instance = MockSimpleTableAnalysis()

        value = bool(0)
        try:
            instance.analysis([])
        except:
            value = bool(1)
            
        self.assertFalse(value, "1. Integracao do 'analysis()'")

if __name__ == '__main__':
    unittest.main()
