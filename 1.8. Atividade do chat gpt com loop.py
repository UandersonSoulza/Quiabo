import os
os.system ("clear")

import random

numero_secreto = random.randint (1, 10) # Gera o número secreto

print("Jogo de Adivinhar.")
print("Vamos brincar?\n")

tentativas = 0 # Contador de tentativas
acertou = False # Variável para controlar o loop

while not acertou: # Enquanto o usuário não acertar...
    palpites = int(input("Escolha um número de 1 a 10: "))
    tentativas += 1 # Contabiliza a tentativa

    if palpites == numero_secreto:
       print(f"🎉 Acertou! Você precisou de {tentativas} tentativa(s)!")
       acertou = True # Sai do loop
    else:
       print(f"Errou! O número era {numero_secreto}. Tente novamente.\n")

print("\nObrigado por jogar!")





