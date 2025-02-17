import os
os.system ("clear")


import random

numero_secreto = random.randint(1, 10)  # Gera o número secreto

print("🎯 Jogo de Adivinhação!")
print("Tente adivinhar o número entre 1 e 10.\n")

tentativas = 0  # Contador de tentativas
acertou = False  # Variável para controlar o loop

while not acertou:  # Enquanto o usuário não acertar...
    palpite = int(input("Escolha um número de 1 a 10: "))
    tentativas += 1  # Contabiliza a tentativa

    if palpite == numero_secreto:
        print(f"🎉 Acertou! Você precisou de {tentativas} tentativa(s)!")
        acertou = True  # Sai do loop
    else:
        print("❌ Errou! Tente novamente.\n")

print("\nObrigado por jogar! 😊")
