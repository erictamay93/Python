"""
Programação Orientada a objeto - POO

- POO é um modelo de paradgma de programação que utiliza mapeamento
de objetos do mundo real para modelos computaconais.

- Paradgma de programação é a forma/metodologia utilizada para
pensar/desenvolver sistemas.

Principais elementos da orientação a orientação a objetos.
- Classe -> Modelo do objeto do mundo real sendo representado computacionalmente.
- Atributo -> Características dp objeto.
- Método -> Comportamento do objeto(funções).
- Construtor -> método especial utilizado para criar objeto.
- Objeto -> instancia da classe.
"""

#--------------------------------------------------------------------------------------------------------------------
"""
POO - Classes 

Em POO , classes nada mais são do que modelos dos objetos do mundo real sendo representados 
computacionalmente.

Classes podem conter: 
    - Atributos -> Repesentam as cracteristicas dos objetos, ou seja , pelos atributos podemos representar 
    computacionalmente os estados de um objeto. No caso da lâmpada, possivelmento iriamos querer saber se a
    lâmpada é de 110 ou 220 volts, se ela é branca, amarela, vermelha, ou de iutra cor, qual é a luminosidade 
    dela etc.
    
    - Métodos -> Representam os comportamentos do objeto, ou seja, as ações que este objeto pode realizar no seu
    sistema. No caso da lampada por exemplo, um comportamento comum que muito provavelmento iriamos querer representar 
    no nosso sistema é o de ligar e desliga a mesma.
    
Para definirmos uma classe me python usamos a palavra reservada 'class' 

OBS: classes sao objetos

"""
#------------------------------------------------------------------------------------------------------------------------------------
"""
POO: Atributos
Atributos representam as características de um projeto. Ou seja, pelos atributos 
nós conseguimos representar  computaconalmete os  estados de um onjeto.

Em python, dividios os atributos em 3 grupos:
    - Atributos de instancia;
    - Atributos de classe;
    - Atributos dinamicos;

# Atributos de instancia:
    São atributos declarados dentro do método construtor.
    __ -> indica que o atributo é private
    self -> É o objeto que está usando o método
    
# Atributos publicos e privados: 
    - Atributos privados so podem ser acessados na propria classe 
    - Por converção todos atributos são publicos 
"""
#print(help(list)) para consultas

class Lampada:
    def __init__(self, voltagem,cor):
        self.__voltagem = voltagem # esta linha indica que o objeto Lampada no atributo Voltagem vai receber voltagem
        self.__cor = cor
        self.__ligada = False

class ContaCorrente:
    def __init__(self,numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

class Usuario:
    def __init__(self,nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

if __name__ == '__main__':
    pass