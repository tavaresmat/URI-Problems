# Author: Matheus Felinto

n = int(input())

contador = 0
lista = []
for i in range(n):
    pokemon = input()
    if pokemon not in lista:
        lista.append(pokemon)
        contador += 1
print("Falta(m) {} pomekon(s)".format(151 - contador))
