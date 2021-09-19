import mysql.connector as data_base

con = data_base.connect(host='localhost',database='cadastro',user='root',password='')

if con.is_connected():
    db_info = con.get_server_info()
    print("conectado ao servidor my sql ",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("conectado ao banco de dados ",linha)

    if con.is_connected():
        cursor.close()
        con.close()
        print("conexão ao mysql foi encerrada")