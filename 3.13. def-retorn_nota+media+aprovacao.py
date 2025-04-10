import os
os.system ("cls||clear")

n1 = 0

def medidi (n1):
    calc = n1 / 2
    return calc

for i in range(2):
    n1 += int(input(f"Digite sua {1+i}º nota: "))

media = medidi (n1)

if media >= 7:
    print("\nVocê foi aprovado!")
else:
    print("\nVocê foi reprovado!")

print (f"Resultado da média: {media}")








