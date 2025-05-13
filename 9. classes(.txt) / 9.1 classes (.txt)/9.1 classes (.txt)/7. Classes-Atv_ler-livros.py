import os
from dataclasses import dataclass

os.system ("cls||clear")

@dataclass
class Livros:
    nome: str
    autor: str
    categoria: str
    preco: float

listas_livros = [] 
QUANTIDADE = 3 

for i in range (QUANTIDADE):
    livros = Livros( 
        nome = input ("Nome: "), 
        autor = input ("Autor: "),
        categoria = input ("categoria: "),
        preco = input ("preco: ")
    )
    listas_livros.append(livros)
    print()

for livros in listas_livros:
    print (f"Nome: {livros.nome}")
    print (f"Autor: {livros.autor}")
    print (f"Categoria: {livros.categoria}")
    print (f"preço: {livros.preco}")
    print()

nome_arquivo = "dados_livros.txt"

print ("Salvando os dados no arquivo...")
with open (nome_arquivo, "a") as arquivo:
    for livros in listas_livros:
        arquivo.write(f"{livros.nome},{livros.autor},{livros.categoria},{livros.preco}\n")

print ("Salvo com sucesso.")

print ("Acessando dados.")
try:
    with open (nome_arquivo, "r") as arquivo: 
        linhas = arquivo.readlines()
        for linha in linhas:
            print (f"- {linha.strip()} -")
except FileNotFoundError:
        print("Arquivo não encontrado.")
