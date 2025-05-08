import os
os.system ("cls||clear")

prato = []
preco = []

while True:
    print("""
        ================= MENU =================
        1 \t Picanha \t\tR$ 25,00
        2 \t Lasanha \t\tR$ 20,00
        3 \t Strogonoff \t\tR$ 18,00
        4 \t Bife acebolado \tR$ 15,00
        5 \t Pão com ovo \t\tR$ 5,00
            """)
    
    opcao = input("Digite o número da opção desejada: ")

    match opcao:
        case "1":
            prato.append("Picanha")
            preco.append(25)
        case "2":
            prato.append("Lasanha")
            preco.append(20)
        case "3":
            prato.append("Strogonoff")
            preco.append(18)
        case "4":
            prato.append("Bife Acebolado")
            preco.append(15)
        case "5":
            prato.append("Pão com ovo")
            preco.append(5)
        case _:
            print ("Invalido!")
        

    os.system ("cls||clear")
    mais = input("Deseja pedir mais? ").lower()

    if mais == "n":
        break       

soma = sum(preco)

print("\n=== Nota Fiscal ===")
print(f"Pratos solicitados: {prato}")
print(f"Valor total da compra: R$ {soma}")















