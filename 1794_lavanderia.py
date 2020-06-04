n = int(input())

la, lb = input().split()
la, lb = int(la), int(lb)

sa, sb = input().split()
sa, sb = int(sa), int(sb)

if (n < la) or (n > lb) or (n < sa) or (n > sb):
    print("impossivel")
else:
    print("possivel")
