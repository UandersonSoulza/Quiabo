import os
from dataclasses import dataclass

os.system ("cls||clear")

@dataclass
class Livro:
    titulo: str
    ano: int

listas_autores = []
QUANTIDADE_AUTORES = 3

@dataclass
class Autor:
    nome: str
    biografia: str
    livro: Livro

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Biografia: {self.biografia}")
        print(f"Título do livro: {self.livro.titulo} || Ano do livro: {self.livro.ano}")

for i in range (QUANTIDADE_AUTORES):
    livro1 = Livro(
    titulo = input("Título do livro: "),
    ano = int(input("Ano do livro: "))
)
    autor1 = Autor(
    input("Autor: "),
    input("Biografia: "),
    livro1)
    listas_autores.append(autor1)
    print()

os.system ("cls||clear")
for i in autor1 (listas_autores):
    autor1.exibir_dados()

# incompleto









