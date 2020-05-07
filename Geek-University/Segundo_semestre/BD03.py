import sqlite3

conexao =sqlite3.connect('livraria.db')
cur=conexao.cursor()
sql="insert into tb_cliente(cpf,nome,idade) values(?,?,?)"

cpf1=input('423')
nome1 = input('Ana')
idade1 = input(23)
cur.execute(sql,(cpf1,nome1,idade1))
conexao.commit()
print("one record added successfully")
cur.close()
conexao.close()