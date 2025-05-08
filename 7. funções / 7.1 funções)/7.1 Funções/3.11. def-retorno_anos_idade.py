import os
os.system ("cls || clear ")

def idade (n1):
    calc = 2025 - n1
    return calc

n1 = int(input("Digite o ano do seu nascimento: "))

subt = idade(n1)

print (f"Você tem {subt} anos.")