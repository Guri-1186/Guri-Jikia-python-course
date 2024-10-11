
"""
2.	დაწერეთ პროგრამა რომელიც მიიღებს არაუარყოფით მთელ რიცხვს - n.  0 <= n < 20.
Პროგრამამ უნდა იპოვოს მიმდევრობის 0-დან n-მდე წევრები. 
Მიმდევრობა განისაზღვრება შემდეგნაირად: ნულოვანი წევრი არის 0,
პირველი წევრი არის 1, ხოლო ყოველი მომდევნო წევრი არის წინა ორი წევრის ჯამი. 
გამოიყენეთ while ციკლი და არ შეიძლება list-ის გამოყენება. 
"""


positive_integer = int(input("Please enter positive integer: "))
if positive_integer < 0 or positive_integer >= 20:
    print("Invalid input, please enter a non negative integer less than 20.")
    exit(1)
 
num_1, num_2 = 0, 1
curr_position = 0

while curr_position <= positive_integer:
    if curr_position == 0:
        print(num_1, end = " ")
    elif curr_position == 1:
        print(num_2, end = " ")
    else:
        num_3 = num_1 + num_2
        print(num_3, end= " ")
        num_1 = num_2
        num_2 = num_3
    curr_position += 1
   
    