import getpass
def logarFuncao():
    print("-" * 30 + str("SISTEMA DE ACADEMIA DO SEU ZÉ") + "-" * 30) 

    host = input("Digite o host que você quer acessar: ")
    user = input("Digite agora o usuário do banco: ")
    password = getpass.getpass("Digite sua senha: ")

    return host,user,password 