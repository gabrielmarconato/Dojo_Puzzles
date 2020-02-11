def pedindo_valor_compra():
    global preço
    preço = float(input("Digite o valor do item comprado: "))

def pedindo_dinheiro_dado():
    global dinheiro
    dinheiro = float(input("Digite o valor dado pelo cliente: "))

def troco_total_a_dar(preço):
    global troco_total
    troco_total = dinheiro - preço

def troco(troco_total):
    z = True

    a,b,c,d,e,f,g,h,i,j,k,l = 100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.25, 0.10, 0.05, 0.01

    nA,nB,nC,nD,nE,nF,nG,nH,nI,nJ,nK,nL = 0,0,0,0,0,0,0,0,0,0,0,0

    while (z == True):
        if (troco_total > a) and (troco_total != 0):
            nA += 1
            troco_total -= a
        elif (a > troco_total >= b) and (troco_total != 0):
            nB += 1
            troco_total -= b
        elif (b > troco_total >= c) and (troco_total != 0):
            nC += 1
            troco_total -= c
        elif (c > troco_total >= d) and (troco_total != 0):
            nD += 1
            troco_total -= d
        elif (d > troco_total >= e) and (troco_total != 0):
            nE += 1
            troco_total -= e
        elif (e > troco_total >= f) and (troco_total != 0):
            nF += 1
            troco_total -= f
        elif (f > troco_total >= g) and (troco_total != 0):
            nG += 1
            troco_total -= g
        elif (g > troco_total >= h) and (troco_total != 0):
            nH += 1
            troco_total -= h
        elif (h > troco_total >= i) and (troco_total != 0):
            nI += 1
            troco_total -= i
        elif (i > troco_total >= j) and (troco_total != 0):
            nJ += 1
            troco_total -= j
        elif (j > troco_total >= k) and (troco_total != 0):
            nK += 1
            troco_total -= k
        elif (k > troco_total >= l) and (troco_total != 0):
            nL += 1
            troco_total -= l
        elif (troco_total == 0):
            z = False
    print("O troco total é: ",nA*a+nB*b+nC*c+nD*d+nE*e+nF*f+nG*g+nH*h+nI*i+nJ*j+nK*k+nL*l , "e deve ser dado em: "
    , nA,"notas de R$100,00", nB,"notas de R$50,00", nC,"notas de R$20,00", nD,"notas de R$10,00", nE,"\n notas de R$5,00", nF,"notas de R$2,00"
    , nG,"moeda de R$1,00", nH,"moedas de 50 centavos"
    , nI,"\n moedas de 25 centavos", nJ,"moedas de 10 centavos", nK,"moedas de 5 centavos", nL,"moedas de 1 centavo")

pedindo_valor_compra()

pedindo_dinheiro_dado()

troco_total_a_dar(preço)

troco(troco_total)