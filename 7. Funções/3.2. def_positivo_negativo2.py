import os
os.system ("cls ||clear ")

def tabua(nue):
    if nue > 0:
        print (f"O número {nue} é positivo.")
    elif nue < 0:
        print (f"O número {nue} é negativo.")
    else:
        print (f"O número {nue} é neutro.")

while True:
    try:
        nu = int(input("Digite um número: "))
        tabua(nu)

    except ValueError:
        print ("Erro tente novamente!")
