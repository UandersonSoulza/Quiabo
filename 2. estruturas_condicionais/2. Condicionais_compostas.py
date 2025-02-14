#limpar terminal
import os 
os.system("clear")

#solicitando dados (entrada)
nome = input("digite seu nome aqui: ")
idade = int(input("digite sua idade aqui: "))


#verificando (processamento)

if idade < 18:
        print ("acesso negado!")
        print ("menoridade! ")
else:
        print ("acesso permitido")
        print ("tenha um bom dia")

#exibindo dados(saída)

print ("==fim==")