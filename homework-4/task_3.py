
"""
3.	Დაწერეთ პროგრამა რომელიც მიიღებს მთელ დადებით რიცხვს. 
Პროგრამამ უნდა იპოვოს და ეკრანზე ერთ ხაზზე დაბეჭდოს ამ რიცხვის ყველა გამყოფი. 
0 < n < 1000. Მაგალითად:
Enter number: 18
1 2 3 6 9 18
"""
positive_integer = int(input("Please enter positive integer:"))

if positive_integer <= 0 or positive_integer >= 1000:
  print("Invalid Input")
  exit(1)

for num in range(1, positive_integer +1):
    if positive_integer % num == 0:
      print(num)