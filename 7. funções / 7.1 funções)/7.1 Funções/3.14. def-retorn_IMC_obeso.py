import os
os.system ("cls||clear")

def imc (peso, alt):
    calc = peso / (alt * alt)
    return calc
    
peso = float(input("Escreva seu peso: "))
alt = float(input("Escreva sua altura: "))

resul = imc (peso, alt)

print (f"Valor do IMC: {resul:.2F}") 
    
if resul < 18.5:
    print ("\nAbaixo do peso! Consulte um nutricionista para orientação.")
elif resul < 25:
    print ("\nPeso normal. Manter hábitos saudáveis!")
elif resul < 30:
    print ("\nSobrepeso! Considere uma dieta balanceada e atividade física.")
elif resul < 35:
    print ("\nObesidade de grau 1! Procure orientação de um profissional de saúde.")
elif resul < 40:
    print ("\nObesidade de grau 2! Consulte um médico para avaliação e orientação.")
else:
    print ("\nObesidade de grau 3! Busque assistência médica imediatamente.")