import sqlite3
database = 'livratia_db'
conexao = sqlite3.connect(database)#Criando a base de dados livrariadb e a conexão
cur=conexao.cursor()
#Criando a tabela tb_cliente dentro da base de dados livraria.db
cur.execute('create table if not exists tb_cliente ('
            'cpf text,'
            'nome text,'
            'idade integer)')
conexao.commit()
cur.close()
conexao.close()

