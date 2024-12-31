import unittest

from src.model.UserInfo.UserInfo import UserInfo

class UserInfoTest(unittest.TestCase):

    def testNewInstance(self):
        instance = UserInfo("user", "password", 0)
        self.assertIsInstance(instance, UserInfo, "1. Devera ser instanciavel corretamente caso possua valores validos")

    def testNewInstanceInvalidUser(self):
        value = bool(0)
        try:
            instance = UserInfo(0, "password", 0)
        except:
            value = bool(1)

        self.assertTrue(value, "2. Devera retornar excessao caso 'user' seja invalido")

    def testNewInstanceInvalidPassword(self):
        value = bool(0)
        try:
            instance = UserInfo("user", 0, 0)
        except:
            value = bool(1)

        self.assertTrue(value, "3. Devera retornar excessao caso 'password' seja invalido")

    def testNewInstanceInvalidCredit(self):
        value = bool(0)
        try:
            instance = UserInfo("user", "password", "credit")
        except:
            value = bool(1)

        self.assertTrue(value, "4. Devera retornar excessao caso 'credit' seja invalido")

    def testSetUser(self):
        instance = UserInfo("user", "password", 0)
        value = bool(0)
        try:
            instance.setUser("newUser")
        except:
            value = bool(1)
            
        self.assertFalse(value, "5. Metodo 'setUser()' devera ser executado corretamente caso possua valor valido")

    def testSetUserInvalid(self):
        instance = UserInfo("user", "password", 0)
        value = bool(0)
        try:
            instance.setUser(0)
        except:
            value = bool(1)
            
        self.assertTrue(value, "6. Metodo 'setUser()' devera retornar excessao caso possua valor invalido")

    def testSetPassword(self):
        instance = UserInfo("user", "password", 0)
        value = bool(0)
        try:
            instance.setPassword("newPassword")
        except:
            value = bool(1)
            
        self.assertFalse(value, "7. Metodo 'setPassword()' devera ser executado corretamente caso possua valor valido")

    def testSetPasswordInvalid(self):
        instance = UserInfo("user", "password", 0)
        value = bool(0)
        try:
            instance.setPassword(0)
        except:
            value = bool(1)
            
        self.assertTrue(value, "8. Metodo 'setPassword()' devera retornar excessao caso possua valor invalido")

    def testSetCredit(self):
        instance = UserInfo("user", "password", 0)
        value = bool(0)
        try:
            instance.setCredit(1)
        except:
            value = bool(1)
            
        self.assertFalse(value, "9. Metodo 'setCredit()' devera ser executado corretamente caso possua valor valido")

    def testSetCreditInvalid(self):
        instance = UserInfo("user", "password", 0)
        value = bool(0)
        try:
            instance.setCredit("credit")
        except:
            value = bool(1)
            
        self.assertTrue(value, "10. Metodo 'setCredit()' devera retornar excessao caso possua valor invalido")

    def testGetUser(self):
        instance = UserInfo("user", "password", 0)
        self.assertEqual(instance.getUser(), "user", "11. Metodo 'getUser()' devera retornar valor corretamente")

    def testGetPassword(self):
        instance = UserInfo("user", "password", 0)
        self.assertEqual(instance.getPassword(), "HASHdrowssap000", "12. Metodo 'getPassword()' devera retornar valor corretamente")

    def testGetCredit(self):
        instance = UserInfo("user", "password", 1)
        self.assertEqual(instance.getCredit(), 1, "13. Metodo 'getCredit()' devera retornar valor corretamente")

if __name__ == '__main__':
    unittest.main()
