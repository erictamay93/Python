from passlib.hash import pbkdf2_sha256 as cryp #importando o necessario para criptografia char256
#-----------------------------------------Pessoa---------------------------------------------------------------------------------------------------
class Pessoa:
    def __init__(self, nome, sobrenome, email,cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    @property
    def sobrenome(self):
        return self.__sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self.__sobrenome = sobrenome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    def nome_comleto(self):
        return f'{self.__nome} {self.__sobrenome}'

#---------------------------------------------Usuario---------------------------------------------------------------------------------------------------
class Usuario(Pessoa):
    contador = 0
    @classmethod # e necessario para criar um método de classe
    def conta_usuarios(cls):# o parametor é a propria classe
        print(f'{cls.contador} usuario(s) no sistema')


    def __init__(self, nome, sobrenome, email, cpf, senha, venda):
        super().__init__(nome,sobrenome, email, cpf)
        self.__venda = venda
        self.__id = Usuario.contador+1
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)# qual string sera incriptada, o ronund mostra quantos embaralhamentos seram feitos salt = parte do texto que será juntada
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')

    @property
    def id(self):
        return self.__id

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def venda(self):
        return self.__venda

    @venda.setter
    def venda(self, venda):
        self.__venda = venda

    #verifica se a senha digitada é igual a senha registrada
    def checa_senha(self,senha):
        if cryp.verify(senha, senha):
            return True
        return False


    def __gera_usuario(self):
        return self.email.split('@')[0] #quebra a string no ponto desejado e devolve o que estava antes do parametro na posiçãozeroda lista


    def mostra_usuario(self,):
        print(f'\n {self.id}'
              f'\n Nome:{self.nome}'
              f'\n Sobrenome:{self.sobrenome}'
              f'\n CPF:{self.cpf}'
              f'\n Email:{self.email}')

#--------------------------------------------Funcionario---------------------------------------------------------------------------------------------------
class Funcionario(Usuario):
    def __init__(self, nome, sobrenome, email, cpf, senha, funcao, venda):
        super().__init__(nome,sobrenome, email,cpf, senha, venda)
        self.__funcao = funcao

    @property
    def funcao(self):
        return self.__funcao

    def mostra_funcao(self):
        print(f'O Funcionario{Usuario.nome} realiza a função de {self.funcao}')

#---------------------------------------------Gerente---------------------------------------------------------------------------------------------------
class Gerente(Usuario):
    def __init__(self, nome, sobrenome, email, cpf, senha,  setor, venda):
        super().__init__(nome,sobrenome, email,cpf, senha, venda)
        self.__setor = setor

    @property
    def setor(self):
        return self.__setor

    @setor.setter
    def setor(self, setor):
        self.__setor = setor

    def mostra_setor(self):
        print(f'O gerente:{Usuario.nome} e responsavel pelo setor:{self.setor}')


    def delUser(self):
        pass

#Cliente---------------------------------------------------------------------------------------------------
class Clinete(Pessoa):
    def __init__(self, nome, sobrenome, email, cpf,compra):
        super().__init__(nome, sobrenome ,email, cpf)
        self.__compra = compra

    @property
    def compra(self):
        return self.__compra

    def mostra_cliente(self):
        print(f'\n Nome:{self.nome}'
              f'\n Sobrenome:{self.sobrenome}'
              f'\n CPF:{self.cpf}'
              f'\n Email:{self.email}'
              f'\n Compra:{self.compra}')


#Venda---------------------------------------------------------------------------------------------------
class Venda:
    def __init__(self, data, hora, produto, cliente, vendedor):
        self.__data = data
        self.__hora = hora
        self.__produto = produto
        self.__cliente = cliente
        self.__vendedor = vendedor

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def hora(self):
        return self.__hora

    @hora.setter
    def hora(self, hora):
        self.__hora = hora

    @property
    def produto(self):
        return self.__produto

    @produto.setter
    def produto(self, produto):
        self.__produto = produto

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def vendedor(self):
        return self.__vendedor

    @vendedor.setter
    def vendedor(self, vendedor):
        self.__vendedor = vendedor


    def nota_fiscal(self):
        pass
    def calc_total(self):
        pass
#Produto---------------------------------------------------------------------------------------------------
class Produto:
    def __init__(self, nome, codigo, preco, descricao, pcusto, imposto):
        self.__nome = nome
        self.__codigo = codigo
        self.__preco = preco
        self.__descricao = descricao
        self.__pcusto = pcusto
        self.__imposto = imposto

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def pcusto(self):
        return self.__pcusto

    @pcusto.setter
    def pcusto(self, pcusto):
        self.__pcusto = pcusto

    @property
    def imposto(self):
        return self.__imposto

    @imposto.setter
    def imposto(self, imposto):
        self.__imposto = imposto

    def lucro(self,imposto, preco, pcusto):
        pimposto = pcusto * imposto/100
        lucro = (pimposto + pcusto) - preco
        return  lucro

    def desconto(self, preco):
        vdesc = int(input('Digite o valor do desconto'))
        desc = (preco * vdesc/100) - preco
        return f'O deconto foi de {desc}'

    def mostra_produto(self):
        print(f'\n Nome:{self.nome}'
              f'\n Código:{self.codigo}'
              f'\n Preço:{self.preco}'
              f'\n Descrição:{self.descricao}'
              f'\n Preço de custo:{self.pcusto}'
              f'\n Porcentagem de impostos:{self.imposto}%')

if __name__ == '__main__':

    user1 = Usuario('Italo','vinicius','italorei7@gmail.com','232.154.687-95','23456',1)
