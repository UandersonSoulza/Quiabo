import os
os.system("clear")

# 2 - Solicitando dados para o usuário
print(""" 
------ CALENDÁRIO ------
1    |\tDomingo       | 
2    |\tSegunda-feira | 
3    |\tTerça-feira   | 
4    |\tQuarta-feira  | 
5    |\tQuinta-feira  | 
6    |\tSexta-feira   |  
7    |\tSábado        | 
""")

numero = int(input("Digite um número: "))

# 3 - Verificando.
match numero:
    case 1 | 7:
        resultado = "Fim de semana."
    case 2 | 3 | 4 | 5 | 6:
        resultado = "Dia útil."
    case _:
        resultado = "Dia inválida."
# 4 - Exibindo resultados.
print ()
print (f"Resultado: {resultado}")