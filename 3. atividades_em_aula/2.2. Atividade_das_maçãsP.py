import os 
os.system("clear")

maca = 1.30

compra = int(input("Quantas maçãs? "))

if compra >= 12:
    maca = 1.00

total = (compra*maca)
print ()
print (f"Foram {compra} maçãs e deu: {total}")


