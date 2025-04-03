import time
import os
os.system ("cls ||clear ")

def tabua(nue):
    for i in range (1,11):
        time.sleep(1)
        print (f"\nTabuada de {nue} x {i} = {nue * i}")

nu = int(input("Digite um número: "))

tabua(nu)




