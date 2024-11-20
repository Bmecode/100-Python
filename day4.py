# DAY4 EXERCISE2
import random
friends=["Burak","Berk","Batu","Rderin","Tugba","Hakan"]
randomNumber=random.randint(0,len(friends)-1)
randomPeople=random.choice(friends)#seçilen yerden random bir elemanı döner.
print(friends[randomNumber])
print(randomPeople)


# DAY4 EXERCISE1
""" import random

a = random.randint(1, 10)#başlangıç ve bitiş değeri dahildir.
b = random.randrange(start=0, stop=17, step=3)#belli bir range aralığı verip sonuncu dahil değil
c=random.random()#0-1 arasında float random bir sayı üretir 1 dahil değildir.
d=random.uniform(1,10) #verdiğimiz aralıkta bir sayı üretir bitiş değeride dahildir.
print(a)
print(b)
print(c)
print(d)
 """