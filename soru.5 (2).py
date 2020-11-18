def asal(n):
    if n <2:
        return False
    for i in range(2,n,1):
        if n % i == 0:
            return False
    return True
    
def super_asal(n):
    if n<=0:
        return True
    if asal(n):
        return super_asal(int(n/10))
    
    
for i in range(10000,100000,1):
    if super_asal(i):
        print(i)
    


    
