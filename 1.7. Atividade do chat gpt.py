import os
os.system ("clear")

import random

numero_secreto = random.randint (1, 10)

print("Jogo de Adivinhar.")
print("Vamos brincar?")

palpite = int(input("\nEscolha um número de 1 a 10: "))

if palpite == numero_secreto:
    print("Acertou!")
else:
    print(f"Errou! O número era {numero_secreto}")







