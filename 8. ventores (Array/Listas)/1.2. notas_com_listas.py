import os
os.system ("cls||clear")

notas = []

for i in range(3):
    nt = float(input(f"Digite sua {1+i}º: "))
    notas.append(nt)

soma = sum(notas)
media = soma / 3
# Mostrando cada nota informafa.

# print ()
# for nt in notas: # ForEach
#     print (f"Nota: {nt}")

# print (f"\nSua {i-1}º nota: {notas[0]}")
# print (f"\nSua {i}º nota: {notas[1]}")
# print (f"\nSua {1+i}º nota: {notas[2]}")

print (f"\nMédia: {media}")
