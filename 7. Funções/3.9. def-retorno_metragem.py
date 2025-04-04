import os
os.system ("cls || clear ")

def metragem (n1):
    metros = n1 * 100
    return metros

n1 = float(input("Escreva alguns números em metros\npara converter em centímetros: "))

resul = metragem (n1)
print (f"\nResultado em centímetros: {resul:.0f}cm")