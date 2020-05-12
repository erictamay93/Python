from passlib.hash import pbkdf2_sha256 as cryp #importando o necessário para criptografia char256
#--------------------------------------------- Pessoa ------------------------------------------------------------------
class Pessoa:
    def __init__(self, nome, sobrenome, email, cpf):
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
        return f'{self.__nome} {self.__sobrenome}.'

#--------------------------------------------- Usuário -----------------------------------------------------------------
class Usuario(Pessoa):
    contador = 0
    @classmethod #é necessário para criar um método de classe
    def conta_usuarios(cls): #o parametro é a propria classe
        print(f'{cls.contador} usuário(s) no sistema.')

    def __init__(self, nome, sobrenome, email, cpf, senha, venda):
        super().__init__(nome, sobrenome, email, cpf)
        self.__venda = venda
        self.__id = Usuario.contador+1
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16) #qual string será incriptada, o ronund mostra quantos embaralhamentos serão feitos; salt = parte do texto que será juntada
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}.')

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
    def checa_senha(self, senha):
        if cryp.verify(senha, senha):
            return True
        return False

    def __gera_usuario(self):
        return self.email.split('@')[0] #quebra a string no ponto desejado e devolve o que estava antes do parametro na posição zero da lista

    def mostra_usuario(self,):
        print(f'\n{self.id}.'
              f'\nNome: {self.nome}.'
              f'\nSobrenome: {self.sobrenome}.'
              f'\nCPF: {self.cpf}.'
              f'\nEmail: {self.email}.')

#--------------------------------------------- Funcionário -------------------------------------------------------------
class Funcionario(Usuario):
    def __init__(self, nome, sobrenome, email, cpf, senha, funcao, venda):
        super().__init__(nome, sobrenome, email, cpf, senha, venda)
        self.__funcao = funcao

    @property
    def funcao(self):
        return self.__funcao

    def mostra_funcao(self):
        print(f'O Funcionário {Usuario.nome} realiza a função de {self.funcao}.')

#--------------------------------------------- Gerente -----------------------------------------------------------------
class Gerente(Usuario):
    def __init__(self, nome, sobrenome, email, cpf, senha, setor, venda):
        super().__init__(nome, sobrenome, email, cpf, senha, venda)
        self.__setor = setor

    @property
    def setor(self):
        return self.__setor

    @setor.setter
    def setor(self, setor):
        self.__setor = setor

    def mostra_setor(self):
        print(f'O gerente {Usuario.nome} é responsável pelo setor {self.setor}.')

    def delUser(self):
        pass

#--------------------------------------------- Cliente -----------------------------------------------------------------
class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, email, cpf, compra):
        super().__init__(nome, sobrenome, email, cpf)
        self.__compra = compra

    @property
    def compra(self):
        return self.__compra

    def mostra_cliente(self):
        print(f'\nNome: {self.nome}.'
              f'\nSobrenome: {self.sobrenome}.'
              f'\nCPF: {self.cpf}.'
              f'\nEmail: {self.email}.'
              f'\nCompra: {self.compra}.')

#--------------------------------------------- Venda -------------------------------------------------------------------
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
        print(f'--------------- Auto Mecanica Simas Turbo ---------------'
              f'\nData: {self.data} Hora: {self.hora}'
              f'\n---------------------------------------------------------'
              f'\nCliente: {self.cliente}'
              f'\n---------------------------------------------------------'
              f'\nProduto: {self.produto}'
              f'\n---------------------------------------------------------'
              f'\nTotal: '
              f'\n---------------------------------------------------------')

#--------------------------------------------- Produto -----------------------------------------------------------------
class Produto:
    contador = 0
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

    def lucro(self, imposto, preco, pcusto):
        pimposto = pcusto * imposto/100
        lucro = (pimposto + pcusto) - preco
        return  lucro

    def desconto(self, preco):
        vdesc = int(input('Digite o valor do desconto: '))
        desc = (preco * vdesc/100) - preco
        return f'O desconto foi de R$ {desc}.'

    def mostra_produto(self):
        print(f'\nNome: {self.nome}.'
              f'\nCódigo: {self.codigo}.'
              f'\nPreço: {self.preco}.'
              f'\nDescrição: {self.descricao}.'
              f'\nPreço de custo: {self.pcusto}.'
              f'\nPorcentagem de impostos: {self.imposto}%.')
#--------------------------------------------- Funções -----------------------------------------------------------------
def menu():
    print(f'O deseja fazer?'
        f'\n1 - Cadastrar produto'
        f'\n2 - Cadastrar usuário'
        f'\n3 - Cadastrar cliente'
        f'\n4 - Alterar produto'
        f'\n5 - Alterar usuário'
        f'\n6 - Alterar cliente'
        f'\n7 - Visualizar produto'
        f'\n8 - Visualizar usuário'
        f'\n9 - Visualizar cliente')
    opcao = input('Digite o número da operção: ')
    return opcao

def cadastra_produto():
    nome = input('Nome do produto: ')
    preco = int(input('Valor do produto: '))
    codigo = int(input('Código de barras: '))
    descricao = input('Descrição do produto: ')
    pcusto = int(input('Valor de fábrica: '))
    imposto = int(input('Porcentagem de impostos: '))

    p = Produto(nome, preco, codigo, descricao, pcusto, imposto)
    print(f'O produto {p.nome} foi cadastrado com sucesso!')
    print(p.__dict__)

def altera_produto(c):
    print('O que deseja alterar?'
          '\n 1 - Atualizar nome'
          '\n 2 - Atualizar preço'
          '\n 3 - Atualizar código de barras'
          '\n 4 - Atualizar descrição'
          '\n 4 - Atualizar valor de fábrica'
          '\n 4 - Atualizar impostos')
    op = input('Digite o número da operação: ')
    if op == '1':
       nnome = (input('Digite o novo nome: '))
       c.nome = nnome
    elif op == '2':
       ncodigo = (input('Digite o preço: '))
       c.codigo = ncodigo
    elif op == '3':
       npreco = (input('Digite o codigo de barras: '))
       c.preco = npreco
    elif op == '4':
       ndescricao = (input('Digite a nova descrição: '))
       c.descricao = ndescricao
    elif op == '5':
       npcusto = (input('Digite o novo preço de fábrica: '))
       c.pcusto = npcusto
    elif op == '6':
       nimposto = (input('Digite a nova porcentagem de impostos: '))
       c.imposto = nimposto


def cadastra_usuario():
    su = input('\n1 - Gerente'
               '\n2 - Funcionário')
    if su =='1':
         nome = input('Informe o nome: ')
         sobrnome =input('Informe o sobrenome: ')
         email = input('Informe o email: ')
         cpf = input('Informe o CPF: ')
         senha = input('Informe a senha: ')
         confirma_senha = input('Confirme a senha: ')
         setor = input('Setor: ')
         venda = 0

         if senha == confirma_senha:
            user = Gerente(nome,sobrnome,email, cpf, senha, setor, venda)
            print(f'Usuário {user.nome_comleto()} criado com sucesso!')
            print(user.__dict__)
         else:
            print('As senhas digitadas estão diferentes.')
            exit(42)
    elif su =='2':

        if su == '1':
            nome = input('Informe o nome: ')
            sobrnome = input('Informe o sobrenome: ')
            email = input('Informe o email: ')
            cpf = input('Informe o CPF: ')
            senha = input('Informe a senha: ')
            confirma_senha = input('Confirme a senha: ')
            cargo = input('Cargo: ')
            venda = 0

            if senha == confirma_senha:
                user = Gerente(nome, sobrnome, email, cpf, senha, cargo, venda)
                print(f'Usuário {user.nome_comleto()} criado com sucesso!')
                print(user.__dict__)
            else:
                print('As senhas digitadas estão diferentes.')
                exit(42)
    else:
        print('Ppção inválida!')

def realiza_venda():
    pass

def cadastra_cliente():
    nome = input('Informe o nome: ')
    sobrnome = input('Informe o sobrenome: ')
    email = input('Informe o email: ')
    cpf = input('Informe o CPF: ')
    compra = 0
    c = Cliente(nome,sobrnome, email, cpf, compra)
    print(f'Usuário {c.nome_comleto()} criado com sucesso!')
    print(c.__dict__)

def altera_cliente(c):
    print('O que deseja alterar?'
          '\n1 - Atualizar nome'
          '\n2 - Atualizar sobrenome'
          '\n3 - Atualizar email'
          '\n4 - Atualizar CPF')
    op = input('Digite o número da operação: ')
    if op == '1':
       nnome = (input('Digite o novo nome: '))
       c.nome = nnome
    elif op == '2':
       nsobrenome = (input('Digite o novo sobrenome: '))
       c.sobrenome = nsobrenome
    elif op == '3':
       nemail = (input('Digite o novo email: '))
       c.email = nemail
    elif op == '4':
       ncpf = (input('Digite o novo CPF: '))
       c.cpf = ncpf

def visualiza_usuario(user):
    Usuario.mostra_usuario(user)

def visualiza_produto(produto):
    Produto.mostra_produto(produto)

def visualiza_cliente(user):
    Cliente.mostra_cliente(user)

if __name__ == '__main__':
#----------------------------------------------Produtos-------------------------------------------------------
   p1 = Produto('Mousepad', 4.99, 789456123, 'Mouse pad com apoio para a mão', 2.49, 1)
   p2 = Produto('Teclado', 4.99, 789455853, 'Teclado mecânico ', 2.49, 2)
   p3 = Produto('Mouse', 4.99, 789452153, 'Mouse óptico sem fio', 2.49, 3)
   p4 = Produto('Monitor', 4.99, 789485223, 'Monitor ASUS 1400X900', 2.49, 1)
   p5 = Produto('Gabinete', 4.99, 789466743, 'Gabinete full tower', 2.49, 1)
   p6 = Produto('Microfone', 4.99, 789459633, 'Microfone de mesa', 2.49, 2)
#---------------------------------------------Usuarios---------------------------------------------------------
   #g1 = Gerente('Italo','Vinicius','cefe@gmail.com','12345678945','123456','Vendedor',0)
   #f1 = Funcionario('João','Batista','jao@gmail.com','65478932145','789456',1,0)
#---------------------------------------------Cliente----------------------------------------------------------
   c1 = Cliente('Juliana', 'Pereira', 'ju@gmail.com', '45696325814', 0)
#--------------------------------------------------------------------------------------------------------------