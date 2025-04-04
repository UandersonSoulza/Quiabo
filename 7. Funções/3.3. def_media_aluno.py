import os
os.system ("cls || clear ")

def calcular_media(nt1, nt2):
    media = (nt1 + nt2) / 2
    print(f"Média: {media:.2f}")
    verificar_aprovacao(media)

def verificar_aprovacao(media):
    if media >= 7:
        print("Você foi Aprovado!")
    else:
        print("Você foi Reprovado!")

nt1 = float(input("Digite a primeira nota: "))
nt2 = float(input("Digite a segunda nota: "))

calcular_media(nt1, nt2)