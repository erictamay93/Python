"""
Poo - Abstração e ecapsulamento

O grande Objetivo da progrmação orientada a objeto é encapsular o código dentro de um grupo logico e hierárquico
 utilizando classes.

        Classe
\---------------------------\
\        Atributos          \
\         Métodos           \
\___________________________\

#  Relembrando Atributos/Métodos privados em python

Imagine que uma classe chamada Pessoa contendo
um atributo privado chamado __nomem e um mértodo privado
chamado __falar()

Esses elementos privados só devem/deveriam ser ascessdos
dentro da classe. mas o python não bloqueia este acesso
fora da classe. com python acontece um fenômeno chamado
Name Mangling, que faz uma alteração na forma de se
acessar os elementos privados, conforme:

_Clase__elemento

Exemplo - acessanso elementos privados fora da classe:
 instancia._Pessoa__nome <- não recomendado
 instancia._Pessoa__falar(): <- não recomendado

Abstração em Poo, é o ato de expor os dadosrelevantes de uma classe, escondendo atributos e métodos
privados de usuario.

"""

class Conta:
    contador = 400
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


# Testando

conta1 = Conta('Jose',150.00,1500)
conta2 = Conta('Angelina',300,200)
conta1.extrato()
conta2.extrato()
conta1.transferir(100,conta2)
conta1.extrato()
conta2.extrato()