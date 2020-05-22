# Author: Matheus

nc = int(input())

for i in range(nc):
    lista = []
    pessoas, salto = input().split()
    pessoas, salto = int(pessoas), int(salto)
    
    lista = list(range(1, pessoas + 1))
    atual = -1

    while (len(lista) > 1):
        lista.pop((atual + salto) % len(lista))
        if len(lista) == 1:
             break
        atual = ((atual + salto) % (len(lista) + 1)) - 1
 
    print("Case {}: {}".format(i + 1, lista[0]))
        
