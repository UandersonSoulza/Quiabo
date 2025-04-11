import os
os.system ("cls||clear")

listas_numeros = []
QUANTIDADE = 5

print ("= LISTA DE COMPRAS =")
for i in range (QUANTIDADE):
    numero =  int(input("Digite um número para lista: "))
    listas_numeros.append(numero)

menor = min(listas_numeros)
max = max(listas_numeros)

# incompleto favor terminar
