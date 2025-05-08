import os
os.system ("cls||clear")

lista = []
QUANTIDADE = 6

def impares_pares (lista):
    par = 0
    impar = 0

    for i in range(QUANTIDADE):
        nu = int(input(f"Digite seu {1+i}º número: "))
        lista.append(nu)
        
        if nu % 2 == 0:
            par += 1
        else:
            impar += 1
            
    return par,impar

resul = impares_pares (lista)
print (f"\nResultado de (Pares, Ímpares): {resul}")







