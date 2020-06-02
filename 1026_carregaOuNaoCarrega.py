# -*- coding: utf-8 -*-

while (True):
    try:
        entrada = input().split()    
    except EOFError:
        break
    a = int(entrada[0])
    b = int(entrada[1])
    print(a^b)