import os 
os.system("clear")

nu1 = float(input("Digite um número: "))
nu2 = float(input("Digite um número: "))

media = (nu1 + nu2) / 2
soma = (nu1 + nu2) 
produto = (nu1 * nu2)

if nu1 < nu2:
    maior_numero = nu1
    menor_numero = nu2
else:
    maior_numero = nu1
    menor_numero = nu2

print(f"\nMédia: {media}")
print(f"Soma: {soma}")
print(f"Produto: {produto}")
print(f"\nMaior número: {maior_numero}")
print(f"Menor número: {menor_numero}")































