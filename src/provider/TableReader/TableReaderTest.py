import unittest

from src.provider.TableReader.TableReader import TableReader
import pandas as pd

class TableReaderTest(unittest.TestCase):

    def testNewInstance(self):
        instance = TableReader("data/test.csv")
        self.assertIsInstance(instance, TableReader, "1. Devera ser instanciavel caso possua valor valido")

    def testOpen(self):
        instance = TableReader("data/test.csv")
        value = bool(0)
        try:
            instance.open()
        except:
            value = bool(1)

        self.assertFalse(value, "2. 'open()' devera retornar valor valido caso arquivo seja valido")

    def testOpenInvalid(self):
        instance = TableReader("data/fake.csv")
        value = bool(0)
        try:
            instance.open()
        except:
            value = bool(1)

        self.assertTrue(value, "3. 'open()' devera retornar excessao caso arquivo seja invalido")

    def testReadAll(self):
        instance = TableReader("data/test.csv")
        instance.open()
        data = instance.readAll()            
        self.assertIsInstance(data, pd.DataFrame, "4. 'readAll()' devera retornar valor valido")

    def testRead(self):
        instance = TableReader("data/test.csv")
        instance.open()
        data = instance.read(1,2)            
        self.assertIsInstance(data, pd.DataFrame, "5. 'read()' devera retornar valor valido caso possua valores validos")

    def testReadStartIndexInvalid(self):
        instance = TableReader("data/test.csv")
        instance.open()
        
        value = bool(0)
        try:
            instance.read("a", 2)
        except:
            value = bool(1)

        self.assertTrue(value, "6. 'read()' devera retornar excessao caso 'startIndex' seja invalido")

    def testReadEndIndexInvalid(self):
        instance = TableReader("data/test.csv")
        instance.open()
        
        value = bool(0)
        try:
            instance.read(1, "a")
        except:
            value = bool(1)

        self.assertTrue(value, "7. 'read()' devera retornar excessao caso 'endIndex' seja invalido")

    def testReadStartIndexNegative(self):
        instance = TableReader("data/test.csv")
        instance.open()
        
        value = bool(0)
        try:
            instance.read(-1, 2)
        except:
            value = bool(1)

        self.assertTrue(value, "8. 'read()' devera ser invalido caso 'startIndex' seja negativo")

    def testReadEndIndexNegative(self):
        instance = TableReader("data/test.csv")
        instance.open()
        
        value = bool(0)
        try:
            instance.read(1, -2)
        except:
            value = bool(1)

        self.assertTrue(value, "9. 'read()' devera ser invalido caso 'endIndex' seja negativo")

    def testReadEndIndexLower(self):
        instance = TableReader("data/test.csv")
        instance.open()
        
        value = bool(0)
        try:
            instance.read(2, 1)
        except:
            value = bool(1)

        self.assertTrue(value, "9. devera ser invalido caso 'endIndex' seja menor que 'startIndex'")

    def testReadEndIndexEqual(self):
        instance = TableReader("data/test.csv")
        instance.open()
        
        value = bool(0)
        try:
            instance.read(1, 1)
        except:
            value = bool(1)

        self.assertTrue(value, "10. devera ser invalido caso 'endIndex' seja igual a 'startIndex'")

if __name__ == '__main__':
    unittest.main()
    