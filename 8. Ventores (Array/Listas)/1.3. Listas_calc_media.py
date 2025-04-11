import os
os.system ("cls||clear")

notas = []
n1 = 0

def medidi (n1):
    calc = n1 / 4
    return calc

for i in range(4):
    n1 += int(input(f"Digite sua {1+i}º nota: "))
    notas.append(n1)

media = medidi (n1)

if media  >= 7:
    resultado = "Você foi Aprovado"
elif media >= 5:
    resultado = "Você está em Recuperação"
else:
    resultado = "Você foi Reprovado"

print(f"\nMédia: {media}")
print(f"Situação: {resultado}")

















