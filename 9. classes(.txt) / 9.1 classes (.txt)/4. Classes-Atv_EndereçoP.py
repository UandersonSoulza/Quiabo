import os
from dataclasses import dataclass

os.system ("cls||clear")

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

listas_clientes = [] # Criando uma lista para adicionar clientes.
QUANTIDADE_CLIENTES = 2 # Constante que define a quantidade de clientes.

print ("Informe os dados do cliente: ")
for i in range (QUANTIDADE_CLIENTES):
    cliente = Cliente( # Instaciando um objeto
        nome = input ("Nome: "), # Não esqueça da vírgula
        email = input ("E-mail: "),
        telefone = input ("Telefone: ") # No ultimo não tem vírgula
    )
    listas_clientes.append(cliente)
    print()

print("\n= Exibindo dados dos clientes =")
for cliente in listas_clientes:
    print (f"Nome: {cliente.nome}")
    print (f"E-mail: {cliente.email}")
    print (f"Telefone: {cliente.telefone}")
    print()

# Salvando em um arquivo .txt
print ("= Salvando os dados dos clientes =")
nome_arquivo = "dados_clientes.txt"

# w -> escrita/salvar/sobrescrever
# a -> escrita/salvar/acumular

with open (nome_arquivo, "w") as arquivo:
    for cliente in listas_clientes:
        arquivo.write(f"{cliente.nome},{cliente.email},{cliente.telefone}\n")


















