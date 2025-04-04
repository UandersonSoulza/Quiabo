import os
os.system ("cls || clear ")

def calcular_media(nota1, nota2):
        media = (nota1 + nota2) / 2
            print(f"Média: {media:.2f}")
                verificar_aprovacao(media)

                def verificar_aprovacao(media):
                    if media >= 7:
                            print("Situação: Aprovado")
                                else:
                                        print("Situação: Reprovado")

                                        # Entrada de notas
                                        nota1 = float(input("Digite a primeira nota: "))
                                        nota2 = float(input("Digite a segunda nota: "))

                                        # Chamada da função principal
                                        calcular_media(nota1, nota2)