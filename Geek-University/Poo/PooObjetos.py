"""
POO - Objetos
# Objetos
    -> São instancias de classe. ou seja, após o mapeamento do objeto real para a sua
    representação computacional, devemos poder criar quantos objetos forem necessarios. Podemos pensar
    os objetos/instancias de uma classe como variáveis do tipo definido da classe.

"""
class Lampada:
    def __init__(self, cor, voltagem, luminisidade):
        self.__cor =cor
        self._voltagem = voltagem
        self.__luminosidade= luminisidade
        self.__ligada = False


class ContaCorrente:
    contador = 4999

    def __init__(self,limite, saldo):
