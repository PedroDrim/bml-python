import unittest

from model.exception.BenchmarkException.BenchmarkException import BenchmarkException

class BenchmarkExceptionTest(unittest.TestCase):

    def testNewInstance(self):
        instance = BenchmarkException("Erro")
        self.assertIsInstance(instance, BenchmarkException, "1. Devera ser instanciavel corretamente")

    def testThrow(self):
        instance = BenchmarkException("Erro")
        value = bool(0)
        try:
            raise instance
        except:
            value = bool(1)
            
        self.assertTrue(value, "2. Devera ser lancado como erro corretamente")

if __name__ == '__main__':
    unittest.main()
