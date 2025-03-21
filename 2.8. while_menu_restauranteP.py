import os
os.system ("cls|clear")

# Apresentar um menu com opções de pratos para o usuário escolher. 
# Perguntar ao usuário se deseja escolher outro prato após cada seleção 
# Quando o usuário decidir parar de pedir, calcular o valor total dos pedidos.
# Perguntar se o usuário deseja incluir uma gorjeta de 10% para o garçom.
# Exibir o nome e o valor dos pratos escolhidos, o valor total dos pedidos, o valor da gorjeta (se houver) e o valor final a pagar.
# termino dps

valor_gojeta = 0
preco_total = 0
preco = 0

while True:
    print(""" 
    ------------ MENU -------------
    Código|\tPrato         |\tValor  
    1     |\tPicanha       | 25,00  
    2     |\tLasanha       | 20,00  
    3     |\tStrongonoff   | 18,00  
    4     |\tBIfe acebolado| 15,00  
    5     |\tPão com ovo   | 5,00  
    """)

    opcao = int(input("Digite o número da opção desejada: "))

    match opcao:
        case 1: 
            prato = "Picanha"
            valor = 25
        case 2:
            prato = "Lasanha"
            valor = 20
        case 3:
            prato = "Strongonoff"
            valor = 18
        case 4:
            prato = "Bife acebolado"
            valor = 15
        case 5:
            prato = "Pão com ovo"
            valor = 5
        case _:
            print  ("opção invalida")
            preco = 0


    preco_total += preco 
    mais_pedidos = input ("Deseja fazer outro pedido? 'S' ou 'N'\n")
    if mais_pedidos == "n":
        break

if preco_total > 0:
    gorjeta_garcom = input ("Deseja pagar os 10% para os garçons? 'S' ou 'N'")
    if gorjeta_garcom == "s":
        valor_gojeta =  preco_total * 0.10

total_pagar = preco_total + valor_gojeta

print ("\n=== Nota fiscal ===")
print (f"=Valor da Gorjeta: R$ {valor_gojeta}")
print (f"=Valor total da compra: R$ {total_pagar}")