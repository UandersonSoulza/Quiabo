import os
from dataclasses import dataclass

# limpa o terminal.
os.system ("cls||clear")

# Criando uma classe.
@dataclass
class Pessoa:
    nome: str
    idade: int

# Aplicando caracteristicas da classe.
pessoa1 = Pessoa(input("Digite seu nome: ")),input("Digite sua idade: ")
pessoa2 = Pessoa("Bob", 25)

print (f"{pessoa1.nome}, idade: {pessoa1.idade} anos.")
print (f"{pessoa2.nome}, idade: {pessoa2.idade} anos.")















