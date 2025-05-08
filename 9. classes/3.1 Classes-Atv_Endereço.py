import os
from dataclasses import dataclass

os.system ("cls||clear")

@dataclass
class Endereco:
    logradouro: str
    numero: int

@dataclass
class Pessoa:
    nome: str
    idade: int
    endereco: Endereco
    
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Endereço: {self.endereco.logradouro}, número: {self.endereco.numero}")

endereco1 = Endereco(
input("Digite o nome da sua rua: "),
input("Digite o numero da sua rua: "))

pessoa1 = Pessoa(
input("Digite seu nome: "),
input("Digite sua idade: "),
endereco1)

os.system ("cls||clear")
pessoa1.exibir_dados()





