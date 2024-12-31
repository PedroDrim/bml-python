import unittest

from src.model.exception.DataReaderException.DataReaderException import DataReaderException

class DataReaderExceptionTest(unittest.TestCase):

    def testNewInstance(self):
        instance = DataReaderException("Erro")
        self.assertIsInstance(instance, DataReaderException, "1. Devera ser instanciavel corretamente")

    def testThrow(self):
        instance = DataReaderException("Erro")
        value = bool(0)
        try:
            raise instance
        except:
            value = bool(1)
            
        self.assertTrue(value, "2. Devera ser lancado como erro corretamente")

if __name__ == '__main__':
    unittest.main()
