import sys

try: 
    valor_dado = int(input("digite um valor inteiro positivo e diremos seus fatores primos: "))
    if valor_dado < 1:
        print("esse é um número inválido, ainda só trabalhamos com números positivos diferentes de zero")
        sys.exit(0)
except ValueError:
    print("Tente digitar um número inteiro desta vez!")
    sys.exit(0)
    

def criar_lista_de_primos_menores_que_valor_dado(valor):
    a = True
    i = 2 
    lista_de_primos = []

    while(a == True):
        if ((i == 2) or (i == 3) or (i == 5) or (i == 7))  and (i <= valor):
            lista_de_primos.append(i)
            i += 1

        if (i%2 != 0) and (i%3 != 0) and (i%5 != 0) and (i%7 != 0) and (i <= valor):
            lista_de_primos.append(i)
            i += 1

        elif ((i%2 == 0) or (i%3 == 0) or (i%5 == 0) or (i%7 == 0)) and (i <= valor) and (i!=3) and (i!=5) and (i!=7):
            i += 1  

        elif (i >= valor):   
            a = False
            break
    return lista_de_primos

def fatorar_valor_dado(lista_de_primos,valor_dado):
    n = 0
    lista_resposta = []

    if valor_dado != 1:
        while(valor_dado != 1):
            if (valor_dado % lista_de_primos[n] == 0):
                lista_resposta.append(lista_de_primos[n])
                valor_dado = valor_dado/lista_de_primos[n]
            if (valor_dado % lista_de_primos[n] != 0):
                n += 1
    return lista_resposta



print('Os fatores primos do número', valor_dado, 'são: ',fatorar_valor_dado(criar_lista_de_primos_menores_que_valor_dado(valor_dado), valor_dado) )