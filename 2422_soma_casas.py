# Matheus Felinto Tavares

def bb(left,right,x):    
    while (left <= right):

        mid = (left + right)//2
        if v[mid] == x:
            return mid
        elif v[mid] > x:
            right = mid -1
        elif v[mid] < x:
            left = mid +1
    return -1

################################

n = int(input())
v = []

for c in range(n):
    v += [int(input())]



soma = int(input())


for i in range(n):
    x = soma - v[i]
    left = 0
    right = n-1
    a = bb(left,right,x)
    if a != -1:
        break

b = soma - v[a]

if b < v[a]:
    print(b,v[a])
elif v[a] < b:
    print(v[a],b)





