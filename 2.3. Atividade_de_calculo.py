import os
os.system("clear")

nu1 = int(input("Digite o primeiro número: "))
nu2 = int(input("Digite o segundo número: "))
op = (input("Digite a operação: "))
resultado = (nu1, nu2)

import os
os.system("clear")

match op:
    case "+":
        print(f"Resultado: {nu1 + nu2}")
    case "-":
        print(f"Resultado: {nu1 - nu2}")
    case "/":
        print(f"Resultado: {nu1 / nu2}")
    case "*":
        print(f"Resultado: {nu1 * nu2}")
    case _:
        print("inválido!")




