import os
os.system ("cls||clear")

# criando listas
listas_de_compras = []
QUANTIDADE = 3

# Solicitando dados para o usuário.
print ("= LISTAS DE COMPRAS =")
for i in range (QUANTIDADE):
    item = input("Digite um item para lista: ")
    listas_de_compras.append(item)

# Exibindo itens da lista de compras
print ("\n= ITENS DA LISTA =")
for i, item in enumerate(listas_de_compras, start=1):
    print(f"{i}º item: {item}")