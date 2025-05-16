import os
import time
from dataclasses import dataclass
os.system ("cls||clear")

funcionarios = []

def verificar_lista_vazia(funcionarios):
    if not funcionarios:
        print("\nA lista está vazia.")
        return True
    return False 

@dataclass
class Registro:
    nome: str
    data_nascimento: int
    cpf: int
    funcao: str

def adicionar(funcionarios):
    registro1 = Registro(
        nome = input("Digite o nome que deseja adicionar: "),
        data_nascimento = int(input("Digite a data de nascimento que deseja adicionar: ")),
        cpf = int(input("Digite seu CPF que deseja adicionar: ")),
        funcao = input("Digite sua função que deseja adicionar: ")
    )
    funcionarios.append(registro1)
    print("Adicionado com sucesso.")

def mostrar(funcionarios):
    if verificar_lista_vazia (funcionarios):
        return

    print ("↓↓↓ Lista dos funcionários ↓↓↓")
    for nome in funcionarios: 
        print (f"{nome}")

def atualizar (funcionarios):
    if verificar_lista_vazia (funcionarios):
        return

    mostrar(funcionarios)
    nome_antigo = input("Digite o nome que deseja atualizar: ")
    try:
        indice = [registro1.nome for registro1 in funcionarios].index(nome_antigo)
        registro1 = funcionarios[indice]
        registro1.nome = input("Digite seu novo nome: ")
    except ValueError:
        print ("Erro")

def excluir(funcionarios):
    if verificar_lista_vazia(funcionarios):
        return
   
    mostrar(funcionarios) 
    nome_excluido = input("Digite o nome que deseja atualizar: ")
    try:
        indice = [registro1.nome for registro1 in funcionarios].index(nome_excluido)
        registro1 = funcionarios[indice]
        funcionarios.remove(registro1)
    except ValueError:
        print ("Erro")
   

while True:
    print("""
             ------ REGISTRO ------
    | \t↓↓↓ Preencher as informações ↓↓↓ | 
    1  | ADICIONAR
    2  | MOSTRAR
    3  | ATUALIZAR
    4  | EXCLUIR
    5  | SAIR
    | \t↑↑↑ ------------------------ ↑↑↑ | 
          """)


    opcao = int(input("Digite uma das opções acima: "))
   
    match opcao:
        case 1:
            adicionar(funcionarios)
        case 2:
            mostrar(funcionarios)
        case 3:
            atualizar(funcionarios)
        case 4:
            excluir(funcionarios)
        case 5:
            print("\nSaindo do programa.")
            break
        case _:
            print("\nOpção inválida. \nTente novamente.")
    if opcao != 1:
        time.sleep(3)
    os.system("cls || clear")