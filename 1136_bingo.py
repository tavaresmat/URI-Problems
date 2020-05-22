#author: Matheus Felinto

passou = False
sair = False

while True:
    n, b = input().split()
    n, b = int(n), int(b)
    if n == 0 and b == 0:
         break
    
    lista = input().split()
    for i in range(b):
        lista[i] = int(lista[i])
    lista.sort()
    
    for numero in range(1, n + 1):
        for bola in range(b):
            if ((lista[bola] + numero) in lista):
                passou = True
                break
            else:
                passou = False
        if passou == False:
            sair = True
            break
                
    if sair == False:
        print("Y")
    else:
        print("N")
        sair = False
