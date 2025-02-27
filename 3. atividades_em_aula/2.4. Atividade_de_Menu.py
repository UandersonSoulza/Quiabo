import os
os.system("clear")

print(""" 
------------ MENU -------------
Código|\tPrato         |\tValor  
1     |\tPicanha       | 25,00  
2     |\tLasanha       | 20,00  
3     |\tStrongonoff   | 18,00  
4     |\tBIfe acebolado| 15,00  
5     |\tPão com ovo   | 5,00  
""")

opcao = int(input("Digite a opção desejada: "))

match opcao:
    case "1":
        prato = "Picanha"
        valor = 25
    case "2":
        prato = "Lasanha"
        valor = 20
    case "3":
        prato = "Strongonoff"
        valor = 18
    case "4":
        prato = "Bife acebolado"
        valor = 15
    case "5":
        prato = "Pão com ovo"
        valor = 5
    case _:
        prato = "opção invalida"
        valor = print ("0")

print (f"Prato: {prato}")
print (f"Valor: R$ {valor}")