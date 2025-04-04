import os
from datetime import datetime
os.system ("cls || clear ")

def idade (n1):
    return datetime.now().year - n1

n1 = int(input("Digite o ano do seu nascimento: "))

subt = idade(n1)

print (f"Você tem {subt} anos.")