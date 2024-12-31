# Excessao responsavel por abstrair erros de parametros invalidos
class InvalidParameterException(Exception):
    
    # Construtor publico da classe
    # @param msg Mensagem de erro
    def __init__(self, msg):
        super().__init__(msg)
