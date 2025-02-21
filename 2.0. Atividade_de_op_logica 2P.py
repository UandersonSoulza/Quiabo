import os 
os.system("clear")

nu1 = int(input("Digite um número: "))
nu2 = int(input("Digite um número: "))

maior_valor = max (nu1, nu2)
menor_valor = min (nu1, nu2)

print ()
print (f"Maior valor: {maior_valor}")
print (f"Menor valor: {menor_valor}")