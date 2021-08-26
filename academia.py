import mysql.connector
import getpass

def conectarnobanco(texto,host,user,password,opcao):
    con = mysql.connector.connect(host=host,database='academia',user=user,password=password)
    if con.is_connected():
        db_info = con.get_server_info()
        print("Conectado ao servidor MySQL versão ",db_info)
        cursor = con.cursor()
        
        cursor.execute(texto)
        #linha = cursor.fetchone()
        linha=  cursor.fetchall()
        print("Conectado ao banco de dados ",linha)
    if opcao == 1:
        con.commit()
    if con.is_connected():
        cursor.close()
        con.close()
        
        print("Conexão ao MySQL foi encerrada")
    return linha

print("-" * 30 + str("SISTEMA DE ACADEMIA DO SEU ZÉ") + "-" * 30) 
host = input("Digite o host que você quer acessar: ")
user = input("Digite agora o usuário do banco: ")
password = getpass.getpass("Digite sua senha: ")

academia  = input("Digite o nome da sua academia: ")

#verificar se a academia existe


if academia == "1":

    print("1-Criar Grupo")
    print("2- Criar Academia")
    print("3-Ver Grupos")
    print("4- Ver Academias")
    opcao = int(input())

    if opcao == 1:

        texto = input("Digite o nome do grupo: ")
        texto = "INSERT INTO GRUPO (NomeGrupo) Values ('{}')".format(texto)
       
    

        print(texto)
        conectarnobanco(texto,host,user,password,1)
        
     
    if opcao == 2:
        nome = input("Digite o nome da academia: ")
        endereco = input("Digite o endereco da academia: ")
        dono = input("Digite o nome do dono da academia: ")
        grupo = input("Digite o nome do grupo da academia: ")
        texto = "SELECT ID_GROUP FROM academia.GRUPO WHERE  NomeGrupo = '" + str(grupo) + "'"
        linha = conectarnobanco(texto,host,user,password,0)
        for x in linha:
            print(x)
            for y in x:
                iddogrupo = y 

        texto = "INSERT INTO ACADEMIA (NomeAcademia,Endereco,Dono,ID_GROUP) Values ('{}','{}','{}',{})".format(nome,endereco,dono,iddogrupo)
       
    

        print(texto)
        conectarnobanco(texto,host,user,password,1)
    if opcao == 3:
        texto = "SELECT * FROM academia.GRUPO"
        linha = conectarnobanco(texto,host,user,password,0)

        
            

    if opcao == 4:
        texto = "SELECT * FROM academia.ACADEMIA"
        linha = conectarnobanco(texto,host,user,password,0)

        for x in linha:
            print(x)




    


else:
    print("O que você deseja fazer?")
    print("1- Cadastrar Aluno")
    print("2- Cadastrar Personal")
    print("O que você deseja fazer?")


print("-" * 30 + str("SISTEMA DE ACADEMIA DO SEU ZÉ") + "-" * 30) 
