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
    - Ao criarmos instâncias/Objetos de uma classe , todas as intâncias terão esses atributos. 
    __ -> indica que o atributo é private
    self -> É o objeto que está usando o método
    
# Atributos publicos e privados: 
    - Atributos privados so podem ser acessados na propria classe 
    - Por converção todos atributos são publicos

# Atributos de Classe
    - São atributos declarados diretamente na classe, ou seja, fora do método construtor.
    geralmente já iniciamos um valor, e este valor é compartilhado entre todas as instancias da classe.
    Ou seja, ao invés de cada  instância da classe ter seus próprios valores como é o caso dos atributos de 
    instâncias, como os atributos de classe todas as instâncias terão o mesmo valor para o atributo.   

# Atributos Dinamicos
    - Um atributo de instância que pode ser criado em tempo de execução, mas o atributo dinamico será exclusivo
    da instância que o criou.
    

"""
#----------------------------------------------------------------------------------------------------------------------

"""
POO - Métodos
-Meétodos(funções) -> representam os comportamentos do objeto. ou seja, as ações que este objeto poder realizar
no seu sitema.

Em python dividimos os métodos em:

# Métodos de instância

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

class Usuario:
    def __init__(self,nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class Produto:
    imposto = 1.05 # Em java atributos de classe são os atributos estaticos
    cont = 0
    def __init__(self, nome, descricao, valor):
        self.id = Produto.cont +1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.cont = self.id

if __name__ == '__main__':
    p1 = Produto("Playstation 4","video-game",13000)
    p1.peso = "800g" # <- atributo de instancia!
    print(p1.__dict__) # <- retorna todos os atributos na forma de um dicionario.
    # o comando 'del' deleta atributos dinamicamente.