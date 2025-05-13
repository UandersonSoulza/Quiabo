import os
from dataclasses import dataclass

os.system ("cls || clear")

@dataclass
class Livros:
    nome: str
    autor: str
    categoria: str
    preco: float

QUANTIDADE = (3)

for i in range (QUANTIDADE):
    
