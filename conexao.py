import mysql.connector

def conectarnobanco(texto,host,user,password,opcao):
    con = mysql.connector.connect(host=host,database='academia',user=user,password=password)
    if con.is_connected():
        db_info = con.get_server_info()
        #print("Conectado ao servidor MySQL versão ",db_info)
        cursor = con.cursor()

        cursor.execute(texto)
        #linha = cursor.fetchone()
        linha=  cursor.fetchall()
        #print("Conectado ao banco de dados ",linha)
    if opcao == 1:
        con.commit()
    if con.is_connected():
        cursor.close()
        con.close()

        #print("Conexão ao MySQL foi encerrada")
    return linha 