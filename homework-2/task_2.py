
"""
task.2 
Დაწერეთ პროგრამა რომელიც მიიღებს ორ რიცხვს, 
დაადგენს პირველი რიცხვი არისთუ არა მეორე რიცხვის ჯერადი და დაბეჭდავს ეკრანზე.
A რიცხვს ეწოდება B რიცხვისჯერადი, თუ A = B * n, სადაც n ნატურალური რიცხვია
"""

num_1 = int(input("please enter first number :"))
num_2 =int(input("please enter second number : "))

if num_1 % num_2 == 0:
  print (f"{num_1} is a multiple of {num_2}")
else:
  print(f"{num_1}  isn't multiple of {num_2}")
  