import os
os.system ("clear")

produto = float(input("Valor do produto: "))
print(""" 
--- FORMA DE PAGAMENTO ---  
1     |\tÁ VISTA |
2     |\tÁ PRAZO | 
""")
pagamento = float(input("Forma de pagamento: "))
os.system ("clear")

match pagamento:
    case 1:
        print ("Forma de pagamento: Á VISTA")
        desconto = produto * 0.10
        total_a_pagar = produto - desconto
        print (f"Valor do desconto: {desconto}")
        print (f"Valor do produto: {produto}")
        print (f"Total a pagar: {total_a_pagar}")
    case 2:
        parcelas = float(input("Digite as parcelas: "))
        os.system ("clear")
        valor_por_parcela = produto / parcelas
        total_a_pagar = produto 
        print (f"Valor do produto: {produto}")
        print ("Forma de pagamento: Á PRAZO")
        print (f"Quantidades de parcelas: {parcelas}")
        print (f"Valor por parcela: {valor_por_parcela:.2f}")
        print (f"Total a pagar: {total_a_pagar}")
    case _:
        print ("Operação inválida")








