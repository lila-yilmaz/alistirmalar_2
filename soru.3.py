#1'den n'ye kadar sayıların çarpılması (n!) 

def faktoriyel(n):
    if n == 1:
        return 1
    else:
        return n*faktoriyel(n-1)
