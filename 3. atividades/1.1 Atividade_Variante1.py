import os 
os.system("clear")

nu1 = float(input("Digite um número: "))
nu2 = float(input("Digite um número: "))

media = (nu1 + nu2) / 2
soma = (nu1 + nu2) 
produto = (nu1 * nu2)

print(f"\nMédia: {media}")
print(f"Soma: {soma}")
print(f"Produto: {produto}")

if nu1 < nu2:
    print(f"Menor valor: {nu1}")
else:
    print(f"\nMenor valor: {nu2}")

if nu1 > nu2:
    print(f"Maior valor: {nu1}")
else:
    print(f"Maior valor: {nu2}")

































