usuario= input("digite o nome de usuario:")
codigo= input("digite o codigo de segurança:")

if usuario == "admin" and codigo == "999":
    print("acesso ao servidor liberado,sistema online")

else:
    print("falha na auteticação,alerta de segurança ligado!")
    