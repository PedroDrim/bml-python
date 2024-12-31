from src.model.exception.InvalidParameterException.InvalidParameterException import InvalidParameterException

# Informacoes do usuario
class UserInfo:

    # Construtor publico da classe
    # @param user Nome do usuario
    # @param password Senha do usuario
    # @param credit Quantidade de creditos do usuario
    def __init__(self, user, password, credit):
        if(not isinstance(user, str)):
            raise InvalidParameterException("'user' e invalido")
        
        if(not isinstance(password, str)):
            raise InvalidParameterException("'password' e invalido")

        if(not isinstance(credit, int) and not isinstance(credit, float)):
            raise InvalidParameterException("'credit' e invalido")

        self.__user = user
        self.__password = password
        self.__credit = credit

    # Obtem o nome do usuario
    # @returns Nome do usuario
    def getUser(self):
        return self.__user

    # Atualiza o nome do usuario
    # @param user Novo nome do usuario
    def setUser(self, user):
        if(not isinstance(user, str)):
            raise InvalidParameterException("'user' e invalido")
        self.__user = user

    # Obtem a senha do usuario criptografada
    # @returns Senha do usuario criptografada
    def getPassword(self):
        return self.__cryptPassword(self.__password)

    # Atualiza a senha do usuario
    # @param password Nova senha do usuario
    def setPassword(self, password):
        if(not isinstance(password, str)):
            raise InvalidParameterException("'password' e invalido")
        self.__password = password

    # Obtem a quantidade de creditos do usuario
    # @returns Quantidade de creditos do usuario
    def getCredit(self):
        return float(self.__credit)

    # Atualiza a quantidade de creditos do usuario
    # @param credit Nova quantidade de creditos do usuario
    def setCredit(self, credit):
        if(not isinstance(credit, int) and not isinstance(credit, float)):
            raise InvalidParameterException("'credit' e invalido")
        self.__credit = credit

    # Metodo privado para encriptar a senha do usuario
    # @param password Senha a ser encriptada
    # @returns Nova senha encriptada
    def __cryptPassword(self, password):
        if(not isinstance(password, str)):
            raise InvalidParameterException("'password' e invalido")
        return "HASH" + password[::-1] + "000"
