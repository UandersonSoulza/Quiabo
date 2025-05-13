import os
from dataclasses import dataclass

os.system ("cls||clear")

@dataclass
class Documentos:
    nome: str
    data_nascimento: int
    rg: int
    cpf: int

listas_doc = [] 
QUANTIDADE = 1

for i in range (QUANTIDADE):
    documentos = Documentos( 
        nome = input("Nome: "), 
        data_nascimento = int(input("Data de nascimnento: ")),
        rg = int(input ("RG: ")),
        cpf = int(input ("CPF: "))
    )
    listas_doc.append(documentos)
    print()

for documentos in listas_doc:
    print (f"Nome: {documentos.nome}")
    print (f"Data de nascimento: {documentos.data_nascimento}")
    print (f"RG: {documentos.rg}")
    print (f"CPF: {documentos.cpf}")
    print()

nome_arquivo = "dados_doc.txt"

print ("Salvando os dados no arquivo...")

def salvando_arq():
    with open (nome_arquivo, "a") as arquivo:
        for documentos in listas_doc:
            arquivo.write(f"{documentos.nome},{documentos.data_nascimento},{documentos.rg},{documentos.cpf}\n")
def lendo_arq ():
    try:
        with open (nome_arquivo, "r") as arquivo: 
            linhas = arquivo.readlines()
            for linha in linhas:
                print (f"- {linha.strip()} -")
    except FileNotFoundError:
            print("Arquivo não encontrado.")

salvando_arq()
print ("Salvo com sucesso.")

lendo_arq()

print ("Acessando dados.")







