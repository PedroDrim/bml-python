import unittest

from src.model.UserInfo.UserInfo import UserInfo

class UserInfoTest(unittest.TestCase):

    def testNewInstance(self):
        instance = UserInfo("user", "password")
        self.assertIsInstance(instance, UserInfo, "1. Devera ser instanciavel corretamente")

    def testSetUser(self):
        instance = UserInfo("user", "password")
        value = bool(0)
        try:
            instance.setUser("newUser")
        except:
            value = bool(1)
            
        self.assertFalse(value, "2. Metodo 'setUser()' devera ser executado corretamente")

    def testSetPassword(self):
        instance = UserInfo("user", "password")
        value = bool(0)
        try:
            instance.setUser("newUser")
        except:
            value = bool(1)
            
        self.assertFalse(value, "3. Metodo 'setPassword()' devera ser executado corretamente")

    def testGetUser(self):
        instance = UserInfo("user", "password")            
        self.assertEqual(instance.getUser(), "user", "4. Metodo 'getUser()' devera retornar valor corretamente")

    def testGetPassword(self):
        instance = UserInfo("user", "password")            
        self.assertEqual(instance.getPassword(), "HASHdrowssap000", "5. Metodo 'getPassword()' devera retornar valor corretamente")

if __name__ == '__main__':
    unittest.main()
