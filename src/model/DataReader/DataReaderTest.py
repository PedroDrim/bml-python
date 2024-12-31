import unittest

from src.model.DataReader.DataReader import DataReader

class MockDataReader(DataReader):
    def readAll(self):
        return 0

    def read(self, startIndex, endIndex):
        return 0


class DataReaderTest(unittest.TestCase):

    def testIntegration(self):
        instance = MockDataReader()

        value = bool(0)
        try:
            instance.readAll()
        except:
            value = bool(1)
            
        self.assertFalse(value, "1. Integracao com 'DataReader'")

if __name__ == '__main__':
    unittest.main()
