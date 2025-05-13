import os
from dataclasses import dataclass

os.system ("cls||clear")

@dataclass
class Funcionario:
    nome: str
    data_admissao: int
    matricula: int
    endereco: str

@dataclass
class Clientes:
    nome: str
    data_nascimento: int
    endereco: str

QUANTIA = 1
lista_fun = []
lista_clie = []

def funcionarrrr():
    for i in range (QUANTIA):
        funcionarios = Funcionario(
            nome = input ("Nome: "),
            data_admissao = int(input ("Data de admissão: ")),
            matricula = int(input ("Matrícula: ")),
            endereco = input ("Endereço:")
        )
        lista_fun.append(funcionarios)
        print()
        
def clientela():        
    for i in range (QUANTIA):
        clientes = Clientes(
            nome = input ("Nome: "),
            data_nascimento = int(input ("Data de nascimento: ")),
            endereco = input ("Endereço:")
        )
        lista_clie.append(clientes)
        print()

funcionarrrr()
clientela()

def resultados():
    for funcionarios in lista_fun:
        print (f"Nome: {funcionarios.nome}")
        print (f"Data de admissão: {funcionarios.data_admissao}")
        print (f"Matrícula: {funcionarios.matricula}")
        print (f"Endereço: {funcionarios.endereco}")
        print()

    for clientes in lista_fun:
        print (f"Nome: {clientes.nome}")
        print (f"Data de admissão: {clientes.data_nascimento}")

        print (f"Endereço: {clientes.endereco}")
        print()

resultados()

nome_arquivo1 = "dados_fun.txt"
nome_arquivo = "dados_clie.txt"

def salvando_arq():
    with open (nome_arquivo1, "a") as arquivo:
        for funcionarios in lista_fun:
            arquivo.write(f"{funcionarios.nome},{funcionarios.data_admissao},{funcionarios.matricula},{funcionarios.endereco}\n")

    with open (nome_arquivo, "a") as arquivo:
        for clientes in lista_clie:
            arquivo.write(f"{clientes.nome},{clientes.data_nascimento},{clientes.endereco}\n")

salvando_arq()











