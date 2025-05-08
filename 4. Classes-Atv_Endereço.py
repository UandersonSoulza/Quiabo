import os
from dataclasses import dataclass

os.system ("cls||clear")

@dataclass
class Endereco:
    logradouro: str 
    cidade: str
    numero: int

@dataclass
class Pessoa:
    nome: str
    email: str
    endereco: Endereco

    def exibir_resul(self):
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Endereço: {self.endereco.logradouro}, Cidade: {self.endereco.cidade}, Número: {self.endereco.numero}")

endereco1 = Endereco(
input("Digite seu endereço: "),
input("Digite sua cidade: ")


)
        
#terminar em casa...   


















