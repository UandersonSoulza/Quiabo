import os 
os.system("clear")

nota1 = float(input("Digite um numero: "))
nota2 = float(input("Digite um numero: "))
nota3 = float(input("Digite um numero: "))

media = (nota1 + nota2 + nota3) / 3

if media < 7:
    print("REPROVADO!")
else:    
    print("APROVADO!")
    

print(f"\nMédia: {media}")























