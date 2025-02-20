import os
os.system ("clear")


# Solicitando dados para o usuario
ob = int(input("Digite sua idade: "))

# Opção 1
 
# Verificando os dados cadastrados com os dados informados pelo usuario
if ob < 18 or ob > 65:
    print ("Você não irá votar!")
else:
    print ("Você irá votar!")