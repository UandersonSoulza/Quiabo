import os 
os.system("clear")

nu1 = float(input("Digite um número: "))
nu2 = float(input("Digite um número: "))

media = (nu1 + nu2) / 2
soma = (nu1 + nu2) 
produto = (nu1 * nu2)   

maior_valor = max (nu1, nu2)
menor_valor = min (nu1, nu2)

if maior_valor == menor_valor:
    print ("São iguais: ")
else:
    print (f"\nMaior valor: {maior_valor}")    
    print (f"Menor valor: {menor_valor}")    

print(f"\nMédia: {media}")
print(f"Soma: {soma}")
print(f"Produto: {produto}")































