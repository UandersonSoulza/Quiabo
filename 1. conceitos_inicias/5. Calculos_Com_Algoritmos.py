import os

#limpa terminal 

os.system("clear")


nome = input("digite seu nome aqui: ")
nome2 = input("digite o nome da sua mãe: ")
idade = int(input("digite sua idade: "))
numero1 = float(input("digite o primeiro número: "))
numero2 = float(input("digite a nota da segunda unidade: "))


#exibindo dados:
print()
print(f"nome: {nome}")
print(f"nome2: {nome2}")
print(f"idade: {idade}")
print(f"soma_dos_numero: {numero1 + numero2}")
print(f"soma_dos_numero: {numero1 - numero2}")
print(f"soma_dos_numero: {numero1 / numero2}")
print(f"soma_dos_numero: {numero1 * numero2}")