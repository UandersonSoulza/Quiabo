import os
os.system ("cls || clear ")

def calc_media (n1,n2):
    calc = (n1 + n2) / 2
    return calc

n1 = int(input("Digite sua primeira nota: "))
n2 = int(input("Digite sua segunda nota: "))

media = calc_media(n1,n2)

print (f"\nResultado da média: {media}")

if media >= 7:
    print ("Aprovado")
else:
    print ("Reprovado")


