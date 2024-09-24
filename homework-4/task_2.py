import random
"""
2.	დაწერეთ პროგრამა, რომელიც მიიღებს მთელ დადებით რიცხვს - n. 
Პროგრამამ, უნდა დააგენერიროს n ცალი შემთვევით მთელი რიცხვი 0  1000 
დიაპაზონიდან და ეკრანზე დაბეჭდოს მათ შორის მაქსიმალური. 0 < n < 30. 
"""
#Solution 1
positive_integer = int(input("Please enter positive integer with max value 29:"))

if positive_integer <= 0 or positive_integer >= 30:
  print("Invalid Input, Please enter a positive number between 1 and 29")
  exit(1)

result = 0 
for num in range(positive_integer):
    rand_int = random.randint(0, 1000)
    if rand_int > result:
      result = rand_int
print("The max value is :",result)




  