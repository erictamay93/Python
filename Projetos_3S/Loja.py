from passlib.hash import pbkdf2_sha256 as cryp #criptografia char256
#Pessoa---------------------------------------------------------------------------------------------------
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

#Usuario---------------------------------------------------------------------------------------------------
class Usuario(Pessoa):
    contador = 0
    @classmethod # e necessario para criar um método de classe
    def conta_usuarios(cls):# o parametor é a propria classe
        print(f'{cls.contador} usuario(s) no sistema')


    def __init__(self, nome, sobrenome, email, cpf, senha):
        super().__init__(nome,sobrenome, email, cpf)
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

    #verifica se a senha digitada é igual a senha registrada
    def checa_senha(self,senha):
        if cryp.verify(senha, senha):
            return True
        return False
    def __gera_usuario(self):
        return self.email.split('@')[0] #quebra a string no ponto desejado e devolve o que estava antes do parametro na posiçãozeroda lista

    def mostra_usuario(self,):
        print(f'\n {self.__id}'
              f'\n Nome:{self.__nome}'
              f'\n Sobrenome:{self.__sobrenome}'
              f'\n CPF:{self.__cpf}'
              f'\n Email:{self.__email}')

#Funcionario---------------------------------------------------------------------------------------------------
class Funcionario(Usuario):
    def __init__(self, nome, sobrenome, email, cpf, senha, funcao):
        super().__init__(nome,sobrenome, email,cpf, senha)
        self.__funcao = funcao

#Gerente---------------------------------------------------------------------------------------------------
class Gerente(Usuario):
    def __init__(self, nome, sobrenome, email, cpf, senha,  setor):
        super().__init__(nome,sobrenome, email,cpf, senha)
        self.__setor = setor

        @property
        def setor(self):
            return self.__setor

        @setor.setter
        def setor(self, setor):
            self.__setor = setor

#Cliente---------------------------------------------------------------------------------------------------
class Clinete(Pessoa):
    def __init__(self, nome, sobrenome, email, cpf):
        super().__init__(nome, sobrenome ,email, cpf)

#Venda---------------------------------------------------------------------------------------------------
class Venda:
    pass

#Produto---------------------------------------------------------------------------------------------------
class Produto:
    pass


user1 = Usuario('Italo','vinicius','italorei7@gmail.com','232.154.687-95','23456')
