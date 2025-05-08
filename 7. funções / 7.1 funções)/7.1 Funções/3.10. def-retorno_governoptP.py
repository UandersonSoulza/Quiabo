import os
os.system ("cls || clear ")

# fazer um programa que solicite o preço de um produto e inflaciona esse preço 
# em 10% se ele for menor que 100 e em 20% se ele for maior ou igual a 100.

def inflaciona(preco):
    valor = 0
    if preco < 100:
        valor = preco * 1.10
    else:
        valor = preco * 1.20
    return valor

preco = float(input("Difite o preço do produto: "))
 
preco_final = inflaciona(preco)

print (f"\nPreço final: {preco_final:.2f}")