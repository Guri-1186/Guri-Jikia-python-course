import random
import math

"""
2.	დაწერეთ პროგრამა რომელიც მიიღებს ნატურალურ რიცხვს n. n > 1. 
პროგრამამ უნდა დააგენერიროს n ცალი წყვილი შემთხვევითი რიცხვი a,b,
სადაც 0<a<1 და 0<b<1. Შემოიღეთ მთვლელი counter,
თუ დაგენერირებული რიცხვი აკმაყოფილებს პირობას math.sqrt(a ** 2 + b ** 2) <=1, 
counter-ის მნიშვნელობა გაზარდეთ 1-ით. 
ეკრანზე დაბეჭდეთ 4 * counter / n. 
"""
number = int(input("Please enter integer (n>1) :"))
if number <= 0:
    print("Invalid input")
    exit(1)
 
counter = 0
for i in range (number):
    a = random.random()
    b = random.random()
 
    if math.sqrt(a ** 2 + b ** 2) <=1:
      counter +=1
    
print(4 * counter / number)
    
