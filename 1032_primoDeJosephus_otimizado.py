# Author: Matheus

def CriaListaPrimos(num):
    primos = [2]
    index = 3
    passou = False
    contador = 1
    while contador < num:
        for item in primos:
            if item**2 > index:
                passou = True
                break
            if (index % item) == 0:
                passou = False
                break
            else:
                passou = True
        if passou == True:
            primos.append(index)
            contador += 1
        index += 2
    return primos


entradas = []
while True:
    pessoas = int(input())
    if pessoas == 0:
        break
    entradas.append(pessoas)

salto = CriaListaPrimos(max(entradas))

for i in entradas:
    lista = list(range(1, i + 1))
    atual = -1
    
    indice = 0
    while (len(lista) > 1):
        lista.pop((atual + salto[indice]) % len(lista))
        if len(lista) <= 1:
             break
        atual = ((atual + salto[indice]) % (len(lista) + 1)) - 1
        indice += 1 
    print(lista[0])

