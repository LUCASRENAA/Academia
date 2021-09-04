import mysql.connector
from conexao import conectarnobanco
from logar import logarFuncao

host,user,password = logarFuncao()
textos = []
texto = """
INSERT INTO GRUPO (NomeGrupo) VALUES("FFF");

"""

textos.append(texto)

texto = """
INSERT INTO ACADEMIA (ID_GROUP, NomeAcademia, quantidadeAlunos, lotacao, Endereco, Dono) VALUES(1, "Forca", 30, 0, "Rua teste", "Lucas");

"""

textos.append(texto)


texto = """
INSERT INTO Pessoa (CPF, Nome_Pessoa, Data_Nascimento, Numero_Celular, Tipo_Sanguineo) VALUES('95639545054', "Izavan", "2021-11-15", "81995021549", "O+");

"""

textos.append(texto)





texto = """
INSERT INTO Pessoa (CPF, Nome_Pessoa, Data_Nascimento, Numero_Celular, Tipo_Sanguineo) VALUES('22342495030', 'Lucas', "2000-05-01", "81995021548", "O-");


"""

textos.append(texto)


texto = """

INSERT INTO CADASTRO_ALUNO (Comprovante, ID_GROUP, CPF) VALUES('Feito', 1, "95639545054");


"""

textos.append(texto)




texto = """

INSERT INTO CADASTRO_PERSONAL (Comprovante, id_ACADEMIA, CPF, Formacao, estadocivil) VALUES('Feito', 1, "22342495030", "Educação física", "S");


"""

textos.append(texto)


texto = """

INSERT INTO EXERCICIOS (Nome, Tipo) VALUES("Supino", "Peito"),("Marinheiro", "Peito"),("Pernada", "Perna"),("Extensora", "Perna"),("Flexão de braço", "Biceps"),("Rosca martelo", "Biceps");
"""

textos.append(texto)



texto = """


INSERT INTO LISTA_EXERCICIOS(DescricaoExercicios, CPF_ALUNO, CPF_PERSONAL, ID_GROUP) VALUES("Opa, se divirta com os exercicios", "95639545054", "22342495030", 1);

"""

textos.append(texto)



texto = """

INSERT INTO EXERCICIOS_LIGACAO (Serie, Repeticao, Intervalo, ID, ID_EXERCICIOS) VALUES('3', 12, 50, 1, 1),('3', 12, 50, 1, 2),('3', 12, 50, 1, 3),('3', 12, 50, 1, 4);


"""

textos.append(texto)






for texto in textos:
        print(texto)
        try:
            conectarnobanco(texto,host,user,password,1)
            print("Tabela criada com sucesso")

        except:
            #print(texto)
            print("Opa, algum erro aconteceu na criação da tabela")
            
            #conectarnobanco(texto,host,user,password)




