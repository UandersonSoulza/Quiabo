import os
os.system ("cls || clear ")

def contar_pares_impares ():
    pares = 0
    impares = 0
    
    for i in range(6):
        n1 = int(input("Digite sua primeira nota: "))
        if n1 % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

resul_par, resul_impar = contar_pares_impares()

print (f"\nO número é par {resul_par}")
print (f"\nO número é ímpar {resul_impar}")


