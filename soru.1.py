#mastermind oyunu 2-98 arası rastgele bir sayı tutma

import random
n = random.randint(10,99)

while (n % 10 == n//10): #basamaklarının farklı olması için
    n = random.randrange(10,99)
    
print(n)
tahmin=0
while tahmin != n:
    tahmin=int(input("10 ile 98 arası (10 ve 98 dahil) bir tahminde bulunun:"))
    if tahmin <= 98 and tahmin >=10 and tahmin % 10 != tahmin//10: #basamaklarının farklı olması için
        dogruyer=0
        yanlisyer=0
        tahmin1=str(tahmin)
        n1=str(n)
        if tahmin1[0] == n1[0]:
            dogruyer+=1
        if tahmin1[0]==n1[1]:
            yanlisyer-=1
        if tahmin1[1] == n1[1]:
            dogruyer+=1
        if tahmin1[1]==n1[0]:
            yanlisyer-=1
        if dogruyer==0 and yanlisyer==0:
            print("skor = 0")
        if dogruyer == 0 and yanlisyer != 0:
            print("Yanlış yer: ",yanlisyer)
        if dogruyer != 0 and yanlisyer == 0:
            print("Doğru yer: ",dogruyer)
    else:
        print("Lütfen 10 ile 98 arasında basamakları aynı omayan bir sayaı giriniz!")

print("Tebrikler! Tahmininiz doğru!")
