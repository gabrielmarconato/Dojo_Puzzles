import sys

ano = int(input("Digite um ano e nós diremos se ele é bissexto: "))

def e_bissexto():
    if (ano % 4 == 0) and ((ano % 100 != 0) or (ano % 400 == 0)):
        print("O ano", ano, "é bissexto" )
    else:
        print("O ano", ano, "não é bissexto" )

e_bissexto()