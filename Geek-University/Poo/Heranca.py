"""
POO - Herança
    A ideia de herança é a de reaproveitar código e extender as nossas classes.

OBS: Com a herança apartir de uma classe existente, nós extendemos outra classe
que passa a herdadr atributos e métodos da classe herdada.


Clinete
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionario
    - nome;
    - sobrenome;
    - cpf;
    - matricula;

OBS:  Quando uma classse herda de outra classe ela herda todos os atributos e métodos da classe herdada

Quando  uma classe herda outra classe, a classe herdada é conhecida por:
    [Pessoa]
    -Super Classe;
    -Classe mãe;
    -Classe Pai;
    -Clasee Base.

Quando uma classe herda de outra classe ela é chamada :
    [Ciente, Funcionario]
    -Sub Classe;
    -Classe filha;
    -Classe especifica


#Sobrescrita de métodos (Overriding)
-> A sobrescrita de métodos, ocorre quando rescrevemos/reimplementamos um método presente na superclasse
em classes filhas.

-> Com 'super()' eu consigo acesso a qualquer método ou atributo da minha SuperClasse
"""
class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

# Cliente herda de Pessoa
class Cliente(Pessoa):

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf) # herdando o condtrutor da superclasse
        self.__renda = renda

class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        return f'Funcionário:{self.__matricula} Nome:{self._Pessoa__nome}'


cliente1 = Cliente('Angelina','Jolie','123.456.789-25',5000)
funcionario1 = Funcionario('Felicity','Jone','7894.561.23-45',1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
