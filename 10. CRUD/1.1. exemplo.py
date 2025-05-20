import os
os.system("cls || clear")

# CRUD em lista.

# Criando uma lista para os nomes.
lista_nomes = []

print("Create - Adicionar / Inserir")
nome = "Marta"
lista_nomes.append(nome)
print(f"O nome {nome} foi inserido com sucesso.")

nome = "Maria"
lista_nomes.append(nome)
print(f"O nome {nome} foi inserido com sucesso.")

#################################

print("\nRead - Ler / Mostrar")
print(lista_nomes)

#################################

print("\nUpdate - Atualizar/Alterar")
nome_para_atualizar = "Marta"
if nome_para_atualizar in lista_nomes:
    novo_nome = "Marta Silva"
    indice = lista_nomes.index(nome_para_atualizar)
    lista_nomes[indice] = novo_nome
    print(f"O nome {nome_para_atualizar} foi atualizado para {novo_nome}")
else:
    print(f"O nome {nome_para_atualizar} não foi encontrado.")
   
print(lista_nomes)

#################################

print("\nDelete - Excluir")
nome_para_excluir = "Maria"
if nome_para_excluir in lista_nomes:
    lista_nomes.remove(nome_para_excluir)
    print(f"{nome_para_excluir} foi removido com sucesso.")
else:
    print(f"O nome {nome_para_excluir} não foi encontrado.")

print(lista_nomes)






















