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

    def checa_lampada(self):
        return self.__ligada
    def liga_desliga(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada =True

class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf


class ContaCorrente:
    contador = 4999

    def __init__(self,limite, saldo, cliente):
        self.__numero = ContaCorrente.contador +1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')



class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.sobrenome = sobrenome
        self.__email = email
        self.sanha = senha




cli1 = Cliente('Italo Vinicius ','123,654,789-46')

cc = ContaCorrente(5000,1000,cli1)
cc.mostra_cliente()

#lamp1 = Lampada('Branca',110,60)
#lamp1.liga_desliga()
#print(f'A lampada esta ligada? {lamp1.checa_lampada()}')
#cc1 = ContaCorrente(5000,2000)
#user1 = Usuario('Falicity','Jones','feleicty@gmail.com','123456')
