import os 

os.system("clear") # Limpa o terminal

# Solicitando dados (Entrada)
idade = int(input("Digite sua idade: "))

# Verificando (Processamento)
# se idade < 18 entao
#      escreval ("Acesso negado!")
# senao
#      escreval ("Acesso permitido!)
# fimse


if idade < 18:
    print("Acesso negado!")
else:    
    print("Acesso permitido!")


# Exibindo dados (saida)
print ("== Fim ==")