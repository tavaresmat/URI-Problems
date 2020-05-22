# -*- coding: utf-8 -*-

# Author: Matheus Felinto Tavares

def FormaLista(indice):
    listapronta = list(range(1, indice + 1))
    return listapronta

def replaceLista(lista):
    a = lista.pop(0)
    lista.append(a)
    return lista

lista = []

while True:
    num = int(input())
    if num == 0:
        break
    lista.append(num)

for num in lista:
    queimados = []
    listaA = FormaLista(num)

    while len(listaA) >= 2:
        queimados += [listaA.pop(0)]
        listaA = replaceLista(listaA)

    print("Discarded cards:", end = "")
    for num in range(len(queimados)):
        if queimados[num] != queimados[-1]:
            print(" {},".format(str(queimados[num])), end = "")
        else:
            print(" {}".format(str(queimados[num])))
    print("Remaining card: ", end = "")
    print(str(listaA[0]))

