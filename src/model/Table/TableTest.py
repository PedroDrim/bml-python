import unittest

from src.model.Table.Table import Table

class TableTest(unittest.TestCase):

    def testNewInstance(self):
        instance = Table("./data/test.csv")
        self.assertIsInstance(instance, Table, "1. Devera ser instanciavel corretamente")

    def testGetFileName(self):
        instance = Table("./data/test.csv")            
        self.assertEqual(instance.getFileName(), "./data/test.csv", "2. Metodo 'getFileName()' devera ser executado corretamente")

    def testGetUserInfoList(self):
        instance = Table("./data/test.csv")            
        self.assertEqual(len(instance.getUserInfoList()), 10, "3. Metodo 'getUserInfoList()' devera retornar valor corretamente")

if __name__ == '__main__':
    unittest.main()
