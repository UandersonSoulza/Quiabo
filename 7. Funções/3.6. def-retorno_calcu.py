import os
os.system ("cls || clear ")

def calc_soma (n1,n2):
    calc = n1 + n2
    return calc

def calc_subtra (n1,n2):
    calc = n1 - n2
    return calc

def calc_divisa (n1,n2):
    calc = n1 / n2
    return calc

def calc_multi (n1,n2):
    calc = n1 * n2
    return calc

def calc_media (n1,n2):
    calc = (n1 + n2) / 2
    return calc

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))

soma = calc_soma(n1,n2)
subt = calc_subtra(n1,n2)
divi = calc_divisa(n1,n2)
mult = calc_multi(n1,n2)
media = calc_media(n1,n2)

print (f"Resultado da soma: {soma}")
print (f"Resultado da subtração: {subt}")
print (f"Resultado da divisão: {divi}")
print (f"Resultado da multiplicação: {mult}")
print (f"Resultado da média: {media}")