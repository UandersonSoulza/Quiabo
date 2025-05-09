import os
from dataclasses import dataclass

os.system ("cls||clear")

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

listas_clientes = []
QUANTIDADE_CLIENTES = 2

print ("Informe os dados do cliente: ")
for i in range (QUANTIDADE_CLIENTES):
    cliente = Cliente(
        nome = input ("Nome: "),
        email = input ("E-mail: "),
        telefone = input ("Telefone: ")
    )
    listas_clientes.append(cliente)
    print()

print("\n= Exibindo dados dos clientes =")
for cliente in listas_clientes:
    print (f"Nome: {cliente.nome}")
    print (f"E-mail: {cliente.email}")
    print (f"Telefone: {cliente.telefone}")
    print()