import os
os.system ("clear")

ob = int(input("Digite sua idade: "))

if ob < 16:
    print ("Ainda não podem votar!")
elif ob < 18:
    print ("Voto opcional.")
elif ob <= 65:
    print ("Voto obrigatório!")
else:
    print ("Não é obrigado a votar.")
    





















