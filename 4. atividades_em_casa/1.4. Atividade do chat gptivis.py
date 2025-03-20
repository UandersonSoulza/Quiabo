import os 
os.system ("clear")

while True: # para tirar o loop, apague o while e break. E organize os code
    try:
        numero = int(input("Digite um número: "))
    
        if numero % 2 == 0:
            print (f"O número {numero} é par.")
        else:
            print (f"O número {numero} é ímpar.")
        break     
    except ValueError:
        print ("Por favor, digite apenas números.")
 














