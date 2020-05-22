lista = []

for cont in range(1,11):
    numero = int(input())
    if numero <= 0:
        lista.append(1)
    else:
        lista.append(numero)

for cont in range(0,10):
    print('X[{}] = {}'.format(cont,lista[cont]))


