import sqlite3

def qtd_registro():
    sql ="SELECT 8 from tb_cliente"
    cur.execute(sql)
    registro=cur.fetchall()
    qtd = len(registro)
    return qtd
conexão
