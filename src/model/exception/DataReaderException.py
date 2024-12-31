# Excessao responsavel por abstrair erros de leitura de dados
class DataReaderException(Exception):
    
    # Construtor publico da classe
    # @param msg Mensagem de erro
    def __init__(self, msg):
        super().__init__(msg)
