import os
os.system ("cls||clear")

lista = []

def minmax (lista):
    maxx = max (lista)
    minn = min (lista)
    return maxx,minn

for i in range(5):
    nu = int(input("Digite um número: "))
    lista.append(nu)

resul = minmax (lista)

os.system ("cls||clear")

for i, nu in enumerate(lista, start=1):
    print (f"{i}º Resultado: {nu}")
print (f"\nMáximo e Mínimo: {resul}")