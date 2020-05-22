# -*- coding: utf-8 -*-

# Author: Matheus Felinto

while True:
    try:
        stringA, stringB = input(), input()
        tamanhoA = len(stringA)
        maior = 0
        for letraA in range(tamanhoA):
            contador = 0
            while stringA[letraA:(letraA + contador) + 1] in stringB and (letraA + contador) < tamanhoA:
                contador += 1
            maior = max(maior, contador)
        print(maior)
    except EOFError:
        break
