A, G, Ra, Rg = input().split()
A = float(A)
G = float(G)
Ra = float(Ra)
Rg = float(Rg)

if (A/Ra) < (G/Rg):
    print('A')
else:
    print('G')