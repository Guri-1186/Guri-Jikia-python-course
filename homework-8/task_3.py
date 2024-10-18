from datetime import datetime

"""
3. დაწერეთ პროგრამა რომელიც მიიღებს თარიღს. 
Პროგრამამ თარიღი უნდა გადაიყვანოს განსხვავებულ 
ფორმატში და დაბეჭდოს ეკრანზე.
"""

user_input = input("Please enter date: for.eg (2024-03-22T19:17:42.956376+04:00):").lower()

var_1 = user_input.replace("t", " ").split(".")[0]
timezone_part = user_input[-6:-3].replace("0","")

print(var_1, timezone_part)
# input - Input: 2024-03-04T11:17:42.000123+04:00
# my output = 2024-03-04 11:17:42 +4

# output - Output: 04-03-2024 11:17:42 +4

