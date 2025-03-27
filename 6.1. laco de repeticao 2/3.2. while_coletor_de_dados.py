import os
os.system ("cls || clear")
media = 0
mue = 0
mais = 0
os.system ("cls || clear")
while True:
    
  match mais:
      case "1":
          id += int(input("Digite sua idade: "))
          sexo = input("Digite sua sexualidade (M/F): ")
          salario = int(input("Digite seu salário: "))
          print("""
  ----- TABELA -----
  Código |  Descrição  
    1    |  Adicionar pessoa       
    2    |  Exibir resultados
    3    |  Sair        
                """)
          mais = input("Deseja adicionar mais pessoas? (Use a tabela acima para responder!) ")
          os.system ("cls || clear")
      case "2":
          break
      case "3":
          break
      case _:
          break


if sexo == "F" and salario >= 5000:
    mue += 1

max = id
min = id

media_sal = salario / 2

print (f"Resultados ↓ \nIdade: {id}\nSexo: {sexo}\nSalário: {salario}")
print (f"Mulheres com salário acima de 5k: {mue}")
print (f"Idade {max} e {min}.")
print (f"Média salarial: {media_sal}")
























