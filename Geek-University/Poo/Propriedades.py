"""
POO - Prorpriedades

-> Em linguagens de programação como java, ao declararmos atributos privado nas classes,
costumamos criar métodos publicos para a manutenção destes atributos. Esses métodos
são conhecidos por getters e setters, ondes os getters retornam o valor do atributo
e os setters açteram o valor do mesmo.

-> deve-se avaliar se ossetters são ou não necessarios

-> Decorator de propriedades(getters) é: @property
Exemplo:
class Conta:
    contador = 0
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador +1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular: {self.__titular} com Limite de{self.__limite}')

    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')
    def sacar(self,valor):
        if valor >0:
            if self.__saldo>= valor:
                self.__saldo -= valor
            else:
                print('saldo insuficiente')
        else:
            print('O valor precisa ser positivo!')
    def transferir(self, valor, conta_destino):
        #1 - remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10 # taxade transferencia
        #2 - Adicionar o valor aconta destino
        conta_destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular


    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__titular = limite

conta1 = Conta('Felicity',3000,5000)
conta2 = Conta('Angelina',2000,4000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma do saldo das contas é {soma}')

print(conta1.__dict__)
conta1.set_limite(1000)
print(conta1.__dict__)

"""

class Conta:
    contador = 0
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador +1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self): # get em python
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite
    @limite.setter # setter em python
    def limite(self,limite):
        self.__limite = limite

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular: {self.__titular} com Limite de{self.__limite}')

    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')
    def sacar(self,valor):
        if valor >0:
            if self.__saldo>= valor:
                self.__saldo -= valor
            else:
                print('saldo insuficiente')
        else:
            print('O valor precisa ser positivo!')
    def transferir(self, valor, conta_destino):
        #1 - remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10 # taxade transferencia
        #2 - Adicionar o valor aconta destino
        conta_destino.__saldo += valor



conta1 = Conta('Felicity',3000,5000)
conta2 = Conta('Angelina',2000,4000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.saldo + conta2.saldo
print(f'A somados saldos das contas é {soma}')

print(conta1.__dict__)
conta1.limite =80000
print(conta1.__dict__)