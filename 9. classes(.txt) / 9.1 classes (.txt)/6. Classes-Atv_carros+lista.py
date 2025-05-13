import os
from dataclasses import dataclass

os.system ("cls || clear")

@dataclass
class Carros:
    marca: str
    modelo: str
    categoria: str
    preco: float

listas_carros = [] 
QUANTIDADE_CARROS = 2 

for i in range (QUANTIDADE_CARROS):
    carritos = Carros( 
        marca = input ("Marca: "), 
        modelo = input ("Modelo: "),
        categoria = input ("Categoria: "),
        preco = input ("Preço: ")
    )
    listas_carros.append(carritos)
    print()

print("\n= Exibindo dados dos clientes =")
for carritos in listas_carros:
    print (f"Marca: {carritos.marca}")
    print (f"Modelo: {carritos.modelo}")
    print (f"Categoria: {carritos.categoria}")
    print (f"Preço: {carritos.preco}")
    print()

print ("= Salvando =")
nome_arquivo = "carros.txt"

with open (nome_arquivo, "a") as arquivo:
    for carritos in listas_carros:
        arquivo.write(f"Marca: {carritos.marca} || Modelo: {carritos.modelo} || Categoria: {carritos.categoria}\n")
