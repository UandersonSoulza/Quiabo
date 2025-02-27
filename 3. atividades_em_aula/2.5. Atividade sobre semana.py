import os
os.system("clear")

print(""" 
------------ CALENDÁRIO -------------  
1     |\tDomingo       | 
2     |\tSegunda-feira | 
3     |\tTerça-feira   | 
4     |\tQuarta-feira  | 
5     |\tQuinta-feira  | 
6     |\tSexta-feira   |  
7     |\tSábado        | 
""")

numero = int (input("Digite um número: "))

match numero:
    case "1":
        print ("Final de semana")
    case "2":
        print ("Dia útil")
    case "3":
        print ("Dia útil")
    case "4":
        print ("Dia útil")
    case "5":
        print ("Dia útil")
    case "6":
        print ("Dia útil")
    case "7":
        print ("Final de semana")
    case _:
        print ("Dia invalido")
 












































