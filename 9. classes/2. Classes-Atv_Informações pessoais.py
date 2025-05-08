import os
from dataclasses import dataclass

os.system ("cls||clear")

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

pessoa1 = Pessoa(
    nome = (input("Digite seu nome: ")),
    idade = int(input("Digite sua idade: ")),
    peso = float(input("Digite seu peso: ")),
    altura = float(input("Digite sua altura: "))
    )

os.system ("cls||clear")
print (f"Nome: {pessoa1.nome}\nIdade: {pessoa1.idade} anos\nPeso: {pessoa1.peso}kg\nAltura: {pessoa1.altura}cm")








