import os 
os.system("clear")

login_cadastrado = "aluno"
senha_cadastrado = "123"

login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

if login_cadastrado == login and senha_cadastrado ==  senha:
    print ("Bem-vindo!")
else:    
    print("Login ou senha inválidos!")