import mysql.connector
import getpass



def conectarnobanco(texto,host,user,password):
    con = mysql.connector.connect(host=host,database='academia',user=user,password=password)
    if con.is_connected():
        db_info = con.get_server_info()
        print("Conectado ao servidor MySQL versão ",db_info)
        cursor = con.cursor()
        
        cursor.execute(texto)
        linha = cursor.fetchone()
        print("Conectado ao banco de dados ",linha)
    if con.is_connected():
        cursor.close()
        con.close()
        print("Conexão ao MySQL foi encerrada")
def criarTabelas(host,user,password):
    print("-" * 30 + "Criando banco de dados" + "-" * 30)




    print("Se conectando ao banco")
    try:
      print("Verificando os dados")
      cnx = mysql.connector.connect(host=host,user=user,password=password)

      mycursor = cnx.cursor()
      mycursor.execute("CREATE DATABASE academia")
      print("Banco criado com sucesso :D")
      
    except:
      print("ERRO EM CRIAR DATABASE ACADEMIA\n verifique se existe um banco de dados chamado academia no seu mysql")


    textos = []
    print("-" * 30 + "Criar tabelas" + "-" *30)

    texto = """
    CREATE TABLE Pessoa (
    CPF VARCHAR(11) PRIMARY KEY ,
    Nome_Pessoa VARCHAR(40),
    Data_Nascimento    DATE,
    Numero_Celular VARCHAR(14),
      Tipo_Sanguineo VARCHAR(3)
    );
    """
    textos.append(texto)



    texto = """
    CREATE TABLE GRUPO (
        ID_GROUP int NOT NULL AUTO_INCREMENT,
      NomeGrupo varchar(255),
        PRIMARY KEY (ID_GROUP)
    );
    """
    textos.append(texto)




    texto = """
    CREATE TABLE CADASTRO_ALUNO (
        ID_CADASTRO_ALUNO int NOT NULL AUTO_INCREMENT,
      Comprovante varchar(255),
          ID_GROUP int,
          CPF VARCHAR(11),

        PRIMARY KEY (ID_CADASTRO_ALUNO),
        FOREIGN KEY (ID_GROUP) REFERENCES GRUPO(ID_GROUP),
        FOREIGN KEY (CPF) REFERENCES Pessoa(CPF)

    );
    """
    textos.append(texto)



    texto = """
    CREATE TABLE ACADEMIA (
        id_ACADEMIA int NOT NULL AUTO_INCREMENT,
          ID_GROUP int,
          
          NomeAcademia VARCHAR(50),

            quantidadeAlunos int,
            lotacao int,

          Endereco VARCHAR(50),
          Dono VARCHAR(50),

        PRIMARY KEY (id_ACADEMIA),
        FOREIGN KEY (ID_GROUP) REFERENCES GRUPO(ID_GROUP)

    );
    """
    textos.append(texto)


    texto = """
    CREATE TABLE FILA_ESPERA (
        ID_FILA_ESPERA int NOT NULL AUTO_INCREMENT,
      Horario DATETIME,
          id_ACADEMIA int,
            
        
          
          Posicao int,
          CPF VARCHAR(11),
              FOREIGN KEY (CPF) REFERENCES Pessoa(CPF),

        PRIMARY KEY (ID_FILA_ESPERA),
        FOREIGN KEY (id_ACADEMIA) REFERENCES ACADEMIA(id_ACADEMIA)

    );
    """
    textos.append(texto)






    texto = """
    CREATE TABLE CADASTRO_PERSONAL (
        ID_CADASTRO_PERSONAL int NOT NULL AUTO_INCREMENT,
      Comprovante varchar(255),

          id_ACADEMIA int,
        CPF VARCHAR(11),

        Formacao VARCHAR(50),
        estadocivil char(1) CHECK (estadocivil IN ('S', 'C', 'D', 'V') ),
        PRIMARY KEY (ID_CADASTRO_PERSONAL),
            FOREIGN KEY (CPF) REFERENCES Pessoa(CPF),
        FOREIGN KEY (id_ACADEMIA) REFERENCES ACADEMIA(id_ACADEMIA)

    );
    """
    textos.append(texto)



    texto = """
    CREATE TABLE LISTA_EXERCICIOS (
        ID int NOT NULL AUTO_INCREMENT,
      DescricaoExercicios varchar(255),
      CPF_ALUNO VARCHAR(11),
      CPF_PERSONAL VARCHAR(11),
          ID_GROUP int,
        PRIMARY KEY (ID),
        FOREIGN KEY (ID_GROUP) REFERENCES GRUPO(ID_GROUP),
        FOREIGN KEY (CPF_ALUNO) REFERENCES Pessoa(CPF),
        FOREIGN KEY (CPF_PERSONAL) REFERENCES Pessoa(CPF)


    );
    """
    textos.append(texto)


    texto = """
    CREATE TABLE EXERCICIOS (
        ID_EXERCICIOS int NOT NULL AUTO_INCREMENT,
      Nome varchar(50),
        
      Tipo varchar(50),
           
        PRIMARY KEY (ID_EXERCICIOS)
    );
    """
    textos.append(texto)


    texto = """
    CREATE TABLE EXERCICIOS_LIGACAO (
        ID_EXERCICIOS_LIGACAO int NOT NULL AUTO_INCREMENT,

        Serie char(1) CHECK (Serie IN ('1', '2', '3', '4') ),
          Repeticao int,
           Intervalo int,

        ID int,
        ID_EXERCICIOS int,
        PRIMARY KEY (ID_EXERCICIOS_LIGACAO),
        FOREIGN KEY (ID) REFERENCES LISTA_EXERCICIOS(ID),
        FOREIGN KEY (ID_EXERCICIOS) REFERENCES EXERCICIOS(ID_EXERCICIOS)


    );
    """
    textos.append(texto)
    for texto in textos:
        print(texto)
        try:
            conectarnobanco(texto,host,user,password)
            print("Tabela criada com sucesso")

        except:
            #print(texto)
            print("Opa, algum erro aconteceu na criação da tabela")
            #conectarnobanco(texto,host,user,password)




    #conectarnobanco(texto,host,user,password)


    print("\n\n\n\n " + "-" * 30 + "CRIADO PARA O SISTEMA DA ACADEMIA DO SEU ZÉ" + "-" * 30)
