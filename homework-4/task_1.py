import random

"""
1.	დაწერეთ პროგრამა რომელიც მიიღებს მოთამაშეების რაოდენობას. 
Პროგრამამ თითოეული მოთამაშისთვის უნდა დააგენერიროს შემთხვევითი 
კამათლების წყვილი და დაბეჭდოს ეკრანზე. Მაგალითად: 
Enter players number: 2
3 4
2 1
"""

number_of_players = int(input("Please enter the number of players : "))

for i in range (number_of_players):
    dice_1 = random.randrange(1,7)
    dice_2 = random.randrange(1,7)
    
    print(dice_1, dice_2)
  
   