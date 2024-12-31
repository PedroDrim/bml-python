import unittest

from src.model.exception.InvalidParameterException.InvalidParameterException import InvalidParameterException

class InvalidParameterExceptionTest(unittest.TestCase):

    def testNewInstance(self):
        instance = InvalidParameterException("Erro")
        self.assertIsInstance(instance, InvalidParameterException, "1. Devera ser instanciavel corretamente")

    def testThrow(self):
        instance = InvalidParameterException("Erro")
        value = bool(0)
        try:
            raise instance
        except:
            value = bool(1)
            
        self.assertTrue(value, "2. Devera ser lancado como erro corretamente")

if __name__ == '__main__':
    unittest.main()
