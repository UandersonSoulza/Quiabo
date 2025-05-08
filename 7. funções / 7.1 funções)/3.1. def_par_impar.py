import os
os.system ("cls ||clear ")

def tabua(nue):
    if nue % 2 == 0:
        print (f"O número {nue} é par")
    else:
        print (f"O número {nue} é ímpar")

nu = int(input("Digite um número: "))
tabua(nu)
