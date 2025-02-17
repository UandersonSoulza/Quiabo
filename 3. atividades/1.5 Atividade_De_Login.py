import os 
os.system("clear") 

login = str(input("Login: "))
senha = float(input("Senha: "))

username = "Quiabo"
password = 5050

if senha == password:
    print ("Bem-vindo!")
else:
    print ("Login e senha invalidos!")

if login == username:
    print ("Acesso concedido!")
else:
    print ("Login e senha invalidos!")