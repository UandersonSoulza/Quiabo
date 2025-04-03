import os
os.system ("clear")

nu1 = int(input("Digite um número: "))
nu2 = int(input("Digite um número: "))
op = str(input("Escolha uma operação: "))

soma = nu1 + nu2
subtr = nu1 - nu2
multi = nu1 * nu2
divisao = nu1 / nu2

while True:
    match op:
        case "+":
            resul = soma
            print (f"Resultado da soma é {resul}.")
            break
        case "/":
            resul = divisao
            print (f"Resultado da divisão é {resul}.")
            break
        case "*":
            resul = multi
            print (f"Resultado da multiplicação é {resul}.")
            break
        case "-":
            resul = subtr
            print (f"Resultado da subtração é {resul}.")
            break
        case _:
            print ("Operação inválida!")
            break