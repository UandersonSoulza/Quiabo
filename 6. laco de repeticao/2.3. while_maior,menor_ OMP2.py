import os
os.system ("cls|clear")

QUANTIDADES_NOTAS = 2
soma = 0

for i in range (QUANTIDADES_NOTAS):
    while True:
        nota = float(input(f"Digite a sua {i+1}ª: "))

        if nota < 0 or nota > 10:
            print ("Inválido, tente novamente.")
        else:
            soma += nota
            break

media = soma / (QUANTIDADES_NOTAS)

print (f"\nMédia total: {media}")










