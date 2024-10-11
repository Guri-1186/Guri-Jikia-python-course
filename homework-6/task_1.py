import random
"""
1.დაწერეთ პროგრამა რომელიც “ჩაიფიქრებს” მთელ რიცხვს 0-დან 100-მდე. 
Მომხმარებელმა უნდა შემოიყვანოს თავისი ვარიანტი ჩაფიქრებული რიცხვის.
 
Თუ მომხმარებლის შემოყვანილი რიცხვი დაემთხვა პროგრამის ჩაფიქრებულ რიცხვს, 
დაბეჭდეთ You are winner. 
Თუ მომხმარებლის შემოყვანილი რიცხვი მეტია, 
კომპიუტერის ჩაფიქრებულ რიცხვზე, დაბეჭდეთ high. 

თუ მომხმარებლის შემოყვანილი რიცხვი ნაკლებია კომპიუტერის ჩაფიქრებულ რიცხვზე, 
დაბეჭდეთ low. 

Მომხმარებელს აქვს მაქსიმუმ 10 მცდელობა. 
Თუ მომხმარებელმა 10 მცდელბაში ვერ გამოიცნო რიცხვი, 
დაბეჭდეთ Computer is winner. 
"""

rand_int = random.randrange(0,100)
print(rand_int)

i = 0
while i < 10:
    user_input = int(input(f"attamptes : {i + 1}/10 - Please enter positive integere : "))
    i+=1
    if rand_int == user_input:
        print("You are winner")
        break
    elif user_input > rand_int:
        print("high")
    elif user_input < rand_int:
        print("low")
    if i == 10:
        print("computer is winner")
       
   
