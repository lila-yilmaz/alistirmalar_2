#Fibonacci dizisinin ilk 30 sayısını ekrana bastırma

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(0,30,1): #ilk 30 sayı --> 0'dan başlarsak 29'a kadar sayması gerekir
    print(fibonacci(i),end=" ")
