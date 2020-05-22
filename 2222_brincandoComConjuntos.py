# Author: Matheus Felinto Tavares

t = int(input())

saida = []

for i in range(t):
    n = int(input())
    conjuntos = []
    
    for j in range(n):
        conjuntos.append(set([int(x) for x in input().split()[1:]]))

    q = int(input())

    for operacao in range(q):
        expressao = [int (x) for x in input().split()]
        
        if expressao[0] == 1:
            intersecao = conjuntos[int(expressao[1]) - 1] & conjuntos[int(expressao[2]) - 1]
            saida.append(len(intersecao))
        else:
            uniao = conjuntos[int(expressao[1]) - 1] | conjuntos[int(expressao[2]) - 1]
            saida.append(len(uniao))

for item in saida:
    print(item)
