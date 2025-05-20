import os 
os.system('clear || cls')
from time import sleep

Lista_Funcionarios = []
Lista_Clientes = []
QUANTIDADES_LIVROS = 3

class Funcionario:
    def __init__(self, Nome, Data_admcao, Matricula, Endereco):
        self.Nome = Nome
        self.Data_admcao = Data_admcao
        self.Matricula = Matricula
        self.Endereco = Endereco
        
    def Imprimir_resultados():
        for funcionario in Lista_Funcionarios:
            print(f'O nome do funcionário é {funcionario.Nome}')
            print(f'A data de admissão é {funcionario.Data_admcao}')
            print(f'A matrícula é {funcionario.Matricula}')
            print(f'O endereço é {funcionario.Endereco}')
            print('---------------------------------------')

class Cliente:
    def __init__(self, Nome, Data_nacimento, Endereco):
        self.Nome = Nome
        self.Data_nacimento = Data_nacimento
        self.Endereco = Endereco

    def Imprimir_resultados():
        for cliente in Lista_Clientes:
            print(f'O nome do cliente é {cliente.Nome}')
            print(f'A data de nascimento é {cliente.Data_nacimento}')
            print(f'O endereço é {cliente.Endereco}')
            print('---------------------------------------')

for i in range(QUANTIDADES_LIVROS):
    Meus_funcionarios = Funcionario(
        Nome = input('Digite o nome do funcionário: '),
        Data_admcao = input('Digite a data de admissão: '),
        Matricula = input('Digite a matrícula: '),
        Endereco = input('Digite o endereço: '))
    Lista_Funcionarios.append(Meus_funcionarios)
    os.system('clear || cls')
Funcionario.Imprimir_resultados()

for i in range(QUANTIDADES_LIVROS):
    Meus_clientes = Cliente(
        Nome = input('Digite o nome do cliente: '),
        Data_nacimento = input('Digite a data de nascimento: '),
        Endereco = input('Digite o endereço: '))
    Lista_Clientes.append(Meus_clientes)
    os.system('clear || cls')
Cliente.Imprimir_resultados()

def Salvar_funcionario():
    dados_funcionario = 'funcionario.txt'
    with open(dados_funcionario, 'a') as arquivo:
        for fun in Lista_Funcionarios: 
            arquivo.write(f'O nome do funcionário é {fun.Nome}\n')
            arquivo.write(f'A data de admissão é {fun.Data_admcao}\n')
            arquivo.write(f'A matrícula é {fun.Matricula}\n')
            arquivo.write(f'O endereço é {fun.Endereco}\n')
            arquivo.write('---------------------------------------\n')
    try:
        with open(dados_funcionario, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                print(linha.strip())
    except FileNotFoundError:
        print(f'Arquivo {dados_funcionario} não encontrado.')
Salvar_funcionario()

def Salvar_cliente():
    dados_cliente = 'cliente.txt'
    with open(dados_cliente, 'a') as arquivo:
        for cli in Lista_Clientes: 
            arquivo.write(f'O nome do cliente é {cli.Nome}\n')
            arquivo.write(f'A data de nascimento é {cli.Data_nacimento}\n')
            arquivo.write(f'O endereço é {cli.Endereco}\n')
            arquivo.write('---------------------------------------\n')
    try:
        with open(dados_cliente, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                print(linha.strip())
    except FileNotFoundError:
        print(f'Arquivo {dados_cliente} não encontrado.')
Salvar_cliente()