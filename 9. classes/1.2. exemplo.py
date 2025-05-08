import os
from dataclasses import dataclass

# limpa o terminal.
os.system ("cls||clear")

# Criando uma classe.
@dataclass
class Pessoa:
    nome: str
    idade: int

@dataclass
class Pet:
    nome: str
    idade: int
    peso: float


# Aplicando caracteristicas da classe.
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)

pet1 = Pet(input("Digite o nome do seu pet: "),input("Digite a idade do seu pet: "),input("Digite o peso do seu pet: "))
pet2 = Pet("tubarão", 6, 9.2)

print ("\n= Dados da pessoa =")
print (f"{pessoa1.nome}, idade: {pessoa1.idade} anos.")
print (f"{pessoa2.nome}, idade: {pessoa2.idade} anos.")

print ("\n= Dados do pet =")
print (f"{pet1.nome}, idade: {pet1.idade} anos, peso: {pet1.peso}")
print (f"{pet2.nome}, idade: {pet2.idade} anos, peso: {pet2.peso}")










