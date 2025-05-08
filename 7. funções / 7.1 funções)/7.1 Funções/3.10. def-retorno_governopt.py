import os
os.system ("cls || clear ")

# fazer um programa que solicite o preço de um produto e inflaciona esse preço 
# em 10% se ele for menor que 100 e em 20% se ele for maior ou igual a 100.

def produto (n1):
    calc = (n1 * 1.10)
    return calc 

def produt2 (n1):
    calc = (n1 * 1.20)
    return calc 

n1 = float(input("Digite o valor do produto: "))

if n1 < 100:
    resul = produto (n1)

if n1 >= 100:
    resul = produt2 (n1)

print (f"\nResultado do produto + imposto: {resul:.2f}")