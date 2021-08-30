import mysql.connector
import getpass
from validate_docbr import CPF
from criartabelas import criarTabelas
cpf = CPF()

def pegarId(linha):
    for x in linha:
                print(x)
                for y in x:
                    iddogrupo = y 
    return iddogrupo
    
def conectarnobanco(texto,host,user,password,opcao):
    con = mysql.connector.connect(host=host,database='academia',user=user,password=password)
    if con.is_connected():
        db_info = con.get_server_info()
        print("Conectado ao servidor MySQL versão ",db_info)
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
        
        print("Conexão ao MySQL foi encerrada")
    return linha

print("-" * 30 + str("SISTEMA DE ACADEMIA DO SEU ZÉ") + "-" * 30) 

host = input("Digite o host que você quer acessar: ")
user = input("Digite agora o usuário do banco: ")
password = getpass.getpass("Digite sua senha: ")

menu = ""
while menu != "5":
    menu = input("""Digite a opção do menu\n
1- Criação do banco(Criar banco e tabelas)\n
2- Administrativo (Criar Academias,Grupos e ver esses grupos)\n
3- Atendente(Organizar a fila de espera e verificar se o aluno é da academia\n
4- Personal trainer(Criar listas de exercicios)\n
5- Sair\n""")

    if menu == "5":
        print("OPS SAINDO")
        print("-" * 30 + str("SISTEMA DE ACADEMIA DO SEU ZÉ") + "-" * 30) 
        
    else:
        if menu == "1":
            criarTabelas(host,user,password)


        #verificar se a academia existe


        if menu == "2":

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
                
                lotacao = int(input("Digite o nome a lotacao da academia: "))
                

                texto = "SELECT ID_GROUP FROM academia.GRUPO WHERE  NomeGrupo = '" + str(grupo) + "'"
                linha = conectarnobanco(texto,host,user,password,0)
                print("Academia está aqui: " + str(linha))
                iddogrupo = pegarId(linha)

                texto = "INSERT INTO ACADEMIA (NomeAcademia,Endereco,Dono,ID_GROUP,quantidadeAlunos,lotacao) Values ('{}','{}','{}',{},0,{})".format(nome,endereco,dono,iddogrupo,lotacao)
            
            

                print(texto)
                conectarnobanco(texto,host,user,password,1)





                texto = "SELECT id_ACADEMIA FROM academia.ACADEMIA WHERE  NomeAcademia = '" + str(nome) + "'"
                linha = conectarnobanco(texto,host,user,password,0)
                print(linha)
                idAcademia = pegarId(linha)


            




            if opcao == 3:
                texto = "SELECT * FROM academia.GRUPO"
                linha = conectarnobanco(texto,host,user,password,0)
                print(linha)

                
                    

            if opcao == 4:
                texto = "SELECT * FROM academia.ACADEMIA"
                linha = conectarnobanco(texto,host,user,password,0)

                for x in linha:
                    print(x)




            


        if menu == "3":
            academia  = input("Digite o nome da sua academia: ")

            vetoracademia = []
            print("Verificando a existencia dessa academia")
            texto = "SELECT * FROM academia.ACADEMIA"
            linha = conectarnobanco(texto,host,user,password,0)
            for i in linha:
                    print(i)
                    if i[2] == academia:
                        vetoracademia = i
            if vetoracademia != []:
                print("Academia existe :D")
                print(i[2])
            else:
                print("Academia não existe")
                
            




            print("O que você deseja fazer?")
            print("1- Cadastrar Pessoa ou Personal")
            print("2- Ver Pessoas")
     

    
            escolher = input("O que você deseja fazer?")
            if escolher == "1":
                cpf_aluno = input("Digite o cpf da pessoa: ")
                while cpf.validate(cpf_aluno) == False:
                    print("Opa, digita o CPF certinho ai amigão :D")
                    cpf_aluno = input("Digite o cpf do pessoa: ")

                nome_aluno = input("Digite o nome do pessoa: ")
                data_aluno = input("Digite a data de nascimento do pessoa: ")
                celular_aluno = input("Digite o  numero de celular do pessoa: ")
                tipo_sanguineo_aluno = input("Digite o tipo sanguineo do pessoa: ")

                texto = "INSERT INTO Pessoa (CPF,Nome_Pessoa,Data_Nascimento,Numero_Celular,Tipo_Sanguineo) Values ('{}','{}','{}','{}','{}')".format(cpf_aluno,nome_aluno,data_aluno,celular_aluno,tipo_sanguineo_aluno)
        
                print(texto)
                conectarnobanco(texto,host,user,password,1)



                texto = "SELECT ID_GROUP FROM academia.ACADEMIA WHERE  NomeAcademia = '" + str(academia) + "'"
                linha = conectarnobanco(texto,host,user,password,0)
                iddogrupo = pegarId(linha)


                texto = "SELECT id_ACADEMIA FROM academia.ACADEMIA WHERE  NomeAcademia = '" + str(academia) + "'"
                linha = conectarnobanco(texto,host,user,password,0)
                iddaacademia = pegarId(linha)


                escolha = input("Aluno ou personal?")
                if escolha == "1":
                    texto = "INSERT INTO CADASTRO_ALUNO (Comprovante,ID_GROUP,CPF) Values ('{}',{},'{}')".format("FEITO",iddogrupo,cpf_aluno)
                    print(texto)
                    conectarnobanco(texto,host,user,password,1)
                if escolha == "2":
                    formacao = input("Digite a formação do Personal: ")
                    estadocivil = input("Digite o estado civil 'S', 'C', 'D', 'V'")
                    texto = "INSERT INTO CADASTRO_PERSONAL (CPF,id_ACADEMIA,Formacao,estadocivil,Comprovante) Values ('{}',{},'{}','{}','Feito')".format(cpf_aluno,iddaacademia,formacao,estadocivil)
                    print(texto)
                    conectarnobanco(texto,host,user,password,1)



            if escolher == "2":
                texto = "SELECT * FROM academia.Pessoa"
                linha = conectarnobanco(texto,host,user,password,0)
                print(linha)

                texto = "SELECT * FROM academia.CADASTRO_ALUNO"
                linha = conectarnobanco(texto,host,user,password,0)
                print(linha)

                texto = "SELECT * FROM academia.CADASTRO_PERSONAL"
                linha = conectarnobanco(texto,host,user,password,0)
                print(linha)

                texto = """SELECT NomeAcademia,quantidadeAlunos
FROM academia.CADASTRO_PERSONAL
INNER JOIN academia.ACADEMIA 
ON CADASTRO_PERSONAL.id_ACADEMIA = ACADEMIA.id_ACADEMIA
"""
                linha = conectarnobanco(texto,host,user,password,0)
                print(linha)














"""
 quantidadeAlunos = int(input("Digite a quantidade de alunos máxima na academia"))
            texto = "INSERT INTO FILA_ESPERA (Horario,id_ACADEMIA,Posicao,CPF) Values (now(),{},0,{},'N','{}')".format(idAcademia,quantidadeAlunos,cpf_aluno)
        
        

            print(texto)
            conectarnobanco(texto,host,user,password,1)
"""