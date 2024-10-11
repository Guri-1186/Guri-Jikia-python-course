"""
1.	დაწერეთ პროგრამა რომელიც მიიღებს ნატურალურ რიცხვს - n ,
სადაც 0 < n < 50 .Პროგრამამ უნდა იპოვოს n მდე არსებული 
ყველა რიცხვის გამყოფები. Დაბეჭდეთ მაქსიმუმ 3 ცალი გამყოფი. 
"""
positive_integer = int(input("Please enter positive integer less than 50 :"))

if positive_integer <= 0 or positive_integer >=50:
    print("Invalid input")
    exit(1)

initial_num = 0
while initial_num < positive_integer:
    initial_num += 1
    print(f"{initial_num}-",  end =" ")
    divisor_count = 0
    divisor = 1
    while divisor <= initial_num:
        if initial_num % divisor == 0:
            print(divisor, end=" ")
            divisor_count+=1
            if divisor_count >= 3:
                break
        divisor+=1
            
  
    print()