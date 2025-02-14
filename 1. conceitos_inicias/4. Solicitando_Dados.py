import os

#limpa terminal 

os.system("clear")

#solicitando dados para o usuarios.

nome = input("digite seu nome aqui: ")
nome2 = input("digite o nome da sua mãe: ")
idade = int(input("digite sua idade: "))
cpf = int(input("digite seu CPF: "))
altura = float(input("digite sua altura: "))
peso = str(input("digite seu peso: "))



#exibindo dados:
print()
print(f"nome: {nome}")
print(f"nome2: {nome2}")
print(f"idade: {idade}")
print(f"cpf: {cpf}")
print(f"altura: {altura}")
print(f"peso: {peso}")