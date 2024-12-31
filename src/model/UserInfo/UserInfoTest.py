import unittest

from src.model.UserInfo.UserInfo import UserInfo

class UserInfoTest(unittest.TestCase):

    def testNewInstance(self):
        instance = UserInfo("user", "password", 0)
        self.assertIsInstance(instance, UserInfo, "1. Devera ser instanciavel corretamente")

    def testSetUser(self):
        instance = UserInfo("user", "password", 0)
        value = bool(0)
        try:
            instance.setUser("newUser")
        except:
            value = bool(1)
            
        self.assertFalse(value, "2. Metodo 'setUser()' devera ser executado corretamente")

    def testSetPassword(self):
        instance = UserInfo("user", "password", 0)
        value = bool(0)
        try:
            instance.setUser("newUser")
        except:
            value = bool(1)
            
        self.assertFalse(value, "3. Metodo 'setPassword()' devera ser executado corretamente")

    def testSetCredit(self):
        instance = UserInfo("user", "password", 0)
        value = bool(0)
        try:
            instance.setCredit(1)
        except:
            value = bool(1)
            
        self.assertFalse(value, "4. Metodo 'setCredit()' devera ser executado corretamente")

    def testGetUser(self):
        instance = UserInfo("user", "password", 0)
        self.assertEqual(instance.getUser(), "user", "5. Metodo 'getUser()' devera retornar valor corretamente")

    def testGetPassword(self):
        instance = UserInfo("user", "password", 0)
        self.assertEqual(instance.getPassword(), "HASHdrowssap000", "6. Metodo 'getPassword()' devera retornar valor corretamente")

    def testGetCredit(self):
        instance = UserInfo("user", "password", 1)
        self.assertEqual(instance.getCredit(), 1, "7. Metodo 'getCredit()' devera retornar valor corretamente")

if __name__ == '__main__':
    unittest.main()
