import os
from dataclasses import dataclass

os.system ("cls||clear")

@dataclass
class Livro:
    titulo: str
    ano: int

@dataclass
class Autor:
    nome: str
    biografia: str
    livro: Livro

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Biografia: {self.biografia}")
        print(f"Título do livro: {self.livro.titulo}|| Ano do livro: {self.livro.ano}")


livro1 = Livro(
titulo = input("Título do livro: "),
ano = int(input("Ano do livro: "))
)

autor1 = Autor(
input("Autor: "),
input("Biografia: "),
livro1)

os.system ("cls||clear")
autor1.exibir_dados()












