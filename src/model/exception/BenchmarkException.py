# Excessao responsavel por abstrair erros de benchmark
class BenchmarkException(Exception):
    
    # Construtor publico da classe
    # @param msg Mensagem de erro
    def __init__(self, msg):
        super().__init__(msg)
