import sqlite3
def qtd_registro():
    sql ="SELECT * from tb_cliente"
    cur.execute(sql)
    registro = cur.fetchall()
    print(registro)
    qtd =len(registro)
    return qtd

conexao =sqlite3.connect('livraria.db')
cur=conexao.cursor()
sql="insert into tb_cliente(cpf, nome, idade) values('122','Paula',21)"
cur.execute(sql)
conexao.commit()
print("one record added successfully")
print('Qtd de registros= ',qtd_registro())
cur.close()
conexao.close()