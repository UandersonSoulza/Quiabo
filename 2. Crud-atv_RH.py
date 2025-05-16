import os
import time
from dataclasses import dataclass
os.system ("cls||clear")

def verificar_lista_vazia(lista_funcionarios):
    if not lista_funcionarios:
        print("\nA lista está vazia.")
        return True
    return False 

@dataclass
class Registro:
    nome: str
    data_nascimento: int
    cpf: int
    funcao: str

def adicionar(lista_funcionarios):
    resgitro1 = Registro(
        nome = input("Digite o nome que deseja adicionar: "),
        data_nascimento = int(input("Digite sua data de nascimento que deseja adicionar: ")),
        cpf = int(input("Digite seu CPF que deseja adicionar: ")),
        funcao = input("Digite sua função que deseja adicionar: ")
    )
    lista_funcionarios.append(resgitro1)
    print("Adicionado com sucesso.")

def mostrar (lista_funcionarios):
    if verificar_lista_vazia (lista_funcionarios):
        return

    print ("↓↓↓ Lista dos funcionários ↓↓↓")
    for nome in lista_funcionarios: 
        print (f"{nome}")
    for data_nascimento in lista_funcionarios:
        print (f"{data_nascimento}")
    for cpf in lista_funcionarios:
        print (f"{cpf}")
    for funcao in lista_funcionarios:
        print (f"{funcao}")

def atualizar (lista_funcionarios):
    if verificar_lista_vazia (lista_funcionarios):
        return

    mostrar(lista_funcionarios)
    nome_antigo = input("Digite o nome que deseja atualizar: ")
    if nome_antigo in lista_funcionarios:
        novo_nome = input(f"Digite o novo nome para {nome_antigo}: ")
        indice = lista_funcionarios.index(nome_antigo)
        lista_funcionarios[indice] = novo_nome
        print(f"{nome_antigo} foi atualizado para {novo_nome}")
    else:
        print(f"\nO nome {nome_antigo} não foi encontrado.")

    data_nascimento_antigo = input("Digite o nome que deseja atualizar: ")
    if data_nascimento_antigo in lista_funcionarios:
        nova_data_nascimento = input(f"Digite o novo nome para {data_nascimento_antigo}: ")
        indice = lista_funcionarios.index(data_nascimento_antigo)
        lista_funcionarios[indice] = nova_data_nascimento
        print(f"{data_nascimento_antigo} foi atualizado para {nova_data_nascimento}")
    else:
        print(f"\nO nome {data_nascimento_antigo} não foi encontrado.")

































while True:
    print("""
             ------ REGISTRO ------
    | \t↓↓↓ Preencher as informações ↓↓↓ | 
    1  | NOME
    2  | DATA DE NASCIMENTO
    3  | CPF
    4  | FUNÇÃO
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
        time.sleep(5)
    os.system("cls || clear")