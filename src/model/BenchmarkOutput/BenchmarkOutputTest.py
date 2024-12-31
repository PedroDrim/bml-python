import unittest

from src.model.BenchmarkOutput.BenchmarkOutput import BenchmarkOutput

class MockBenchmarkOutput(BenchmarkOutput):
    def startState(self, tag):
        return 0

    def endState(self, tag):
        return 0

    def resultByTag(self, tag, format):
        return 0

    def result(self, format):
        return 0

    def export(self, fileName, format):
        return 0


class BenchmarkOutputTest(unittest.TestCase):

    def testIntegration(self):
        instance = MockBenchmarkOutput()

        value = bool(0)
        try:
            instance.startState(0)
        except:
            value = bool(1)
            
        self.assertFalse(value, "1. Integracao com 'BenchmarkOutput'")

if __name__ == '__main__':
    unittest.main()
