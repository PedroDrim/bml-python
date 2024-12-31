import unittest

from src.model.TimeFormat.TimeFormat import TimeFormat


class TimeFormatTest(unittest.TestCase):

    def testSegundos(self):
        value = bool(0)
        try:
            TimeFormat.SEGUNDOS
        except:
            value = bool(1)
            
        self.assertFalse(value, "1. 'TimeFormat.SEGUNDOS' e valido")

    def testMilissegundos(self):
        value = bool(0)
        try:
            TimeFormat.MILLISEGUNDOS
        except:
            value = bool(1)
            
        self.assertFalse(value, "1. 'TimeFormat.MILLISEGUNDOS' e valido")

    def testNanossegundos(self):
        value = bool(0)
        try:
            TimeFormat.NANOSSEGUNDOS
        except:
            value = bool(1)
            
        self.assertFalse(value, "1. 'TimeFormat.NANOSSEGUNDOS' e valido")

if __name__ == '__main__':
    unittest.main()
