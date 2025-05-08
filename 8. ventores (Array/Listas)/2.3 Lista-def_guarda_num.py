import os
os.system ("cls||clear")

lista = []
QUANTIDADE = 5

def uand_souza ():

    for i in range(QUANTIDADE):
        nu = int(input(f"Digite seu {1+i}º número: "))
        lista.append(nu)
    return lista

def calc (lista):
    for i in lista:
        if i < 0:
            i = 0
        print (f"{i}")
    
medica_gostosa = uand_souza()
print ()
calc (medica_gostosa)


















