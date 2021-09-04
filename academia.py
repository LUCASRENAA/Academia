import mysql.connector
import getpass
from validate_docbr import CPF
from criartabelas import criarTabelas
from conexao import conectarnobanco

cpf = CPF()



def pegarId(linha):
    for x in linha:
                print(x)
                for y in x:
                    iddogrupo = y 
    return iddogrupo


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
                data_aluno = input("Digite a data de nascimento do pessoa(formato: AAAA-MM-DD): ")
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


                escolha = input("Aluno ou personal? 1 para aluno e 2 para Personal")
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

                texto = """
            


SELECT Nome_Pessoa,NomeAcademia,Comprovante,Formacao 
FROM academia.CADASTRO_PERSONAL 
INNER JOIN academia.ACADEMIA
INNER JOIN academia.Pessoa
ON id_ACADEMIA = ACADEMIA.id_ACADEMIA
ON CADASTRO_PERSONAL.CPF = Pessoa.CPF


"""
                linha = conectarnobanco(texto,host,user,password,0)
                print(linha)
        if menu == "4":
            print("Painel do Personal Trainer" + "-" * 10 )
            cpf_personal = input("Digite aqui o seu cpf aqui")
            print("verificando seu usuario...")





            opcao_personal = input("O que você quer fazer? \n1- Criar uma lista de exercicio 2-Editar uma")
            texto = "SELECT id_ACADEMIA FROM academia.CADASTRO_PERSONAL where CPF = {}".format(cpf_personal) 
            linha = conectarnobanco(texto,host,user,password,0)
            id_academia = pegarId(linha)
            #print(linha)

            texto = "SELECT ID_GROUP FROM academia.ACADEMIA where id_ACADEMIA = {}".format(id_academia) 
            linha = conectarnobanco(texto,host,user,password,0)
            id_grupo = pegarId(linha)

            #print(linha)


            print(" id do grupo: " + str(id_grupo))
            print(" id do academia: " + str(id_academia))

            if opcao_personal == "1":
                descricao = input("digite a descrição dos exercicios: ")
                cpf_aluno = input("cpf aluno: ")

                texto = "INSERT INTO LISTA_EXERCICIOS (DescricaoExercicios,CPF_PERSONAL,ID_GROUP,CPF_ALUNO) Values ('{}','{}',{},'{}')".format(descricao,cpf_personal,id_grupo,cpf_aluno)
                conectarnobanco(texto,host,user,password,1)

                opcao_exercicio = "0"
                while opcao_exercicio != "4":
                    opcao_exercicio = input("1- criar exercicio\n2- escolher\n3-adicionar numa lista\n4-sair")
                    
                    if opcao_exercicio == "1":
                        print("alo")
                        nome_Exercicio = input("Nome do exercicio: ")
                        tipo_Exercicio = input("Tipo do exercicio: ")

                        texto = "INSERT INTO EXERCICIOS (Nome,Tipo) Values ('{}','{}')".format(nome_Exercicio,tipo_Exercicio)
                        conectarnobanco(texto,host,user,password,1)

                    if opcao_exercicio == "2":
                        texto = "SELECT  * FROM EXERCICIOS"
                        linha = conectarnobanco(texto,host,user,password,0)
                        print(linha)

                    if opcao_exercicio == "3":

                        serie = input("serie: ")
                        repeticao = input("repeticao: ")
                        intervalo = input("intervalo: ")

                        texto = "SELECT ID FROM academia.LISTA_EXERCICIOS WHERE  CPF_ALUNO = '" + str(cpf_aluno) + "'"
                        linha = conectarnobanco(texto,host,user,password,0)
                        print("Academia está aqui: " + str(linha))
                        id_lista = pegarId(linha)
                        nome_exercicio = input("nome exercicio: ")


                        texto = "SELECT ID_EXERCICIOS FROM academia.EXERCICIOS WHERE  Nome = '" + str(nome_exercicio) + "'"
                        linha = conectarnobanco(texto,host,user,password,0)
                        print("Academia está aqui: " + str(linha))
                        id_exercicio = pegarId(linha)


                        texto = "INSERT INTO EXERCICIOS_LIGACAO (Serie,Repeticao,Intervalo,ID,ID_EXERCICIOS) Values ('{}',{},{},{},{})".format(serie,repeticao,intervalo,id_lista,id_exercicio)
                        conectarnobanco(texto,host,user,password,1)







        













"""
 quantidadeAlunos = int(input("Digite a quantidade de alunos máxima na academia"))
            texto = "INSERT INTO FILA_ESPERA (Horario,id_ACADEMIA,Posicao,CPF) Values (now(),{},0,{},'N','{}')".format(idAcademia,quantidadeAlunos,cpf_aluno)
        
        

            print(texto)
            conectarnobanco(texto,host,user,password,1)
"""