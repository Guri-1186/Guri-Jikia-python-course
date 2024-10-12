"""
დაწერეთ პროგრამა რომელიც მიიღებს არაუარყოფით მთელ რიცხვს - n. 
0 <= n < 10000 და დაბეჭდავს ამ რიცხვის შებრუნებულ მნიშვნელობას 
და ამ რიცხვში შემავალი ციფრების ჯამს. გამოიყენეთ while ციკლი
"""
positive_integer = int(input("Please enter positive integer with max value 1000 :"))

if positive_integer <= 0 or positive_integer > 1000:
    print("Invalid input")
    exit(1)
    
reversed_num = 0 
sum_of_num = 0 

while positive_integer > 0:
    digit = positive_integer % 10 
    reversed_num = reversed_num * 10 + digit 
    positive_integer//= 10 
   
    sum_of_num += digit
    
print(reversed_num)
print(sum_of_num)

