

"""
3. დაწერეთ პროგრამა რომელიც მიიღებს თარიღს. 
Პროგრამამ თარიღი უნდა გადაიყვანოს განსხვავებულ 
ფორმატში და დაბეჭდოს ეკრანზე.
"""

user_input = input("Please enter date: for.eg (2024-03-22T19:17:42.956376+04:00):").lower()

date_part = user_input.replace("t", " ").split(".")[0].split(" ")[0]
year, month, day = date_part.split("-")
formated_date = f"{day}-{month}-{year}"
time_part =user_input.replace("t", " ").split(".")[0].split(" ")[1]
timezone_part = user_input[-6:-3].replace("0","")


# Input: 2024-03-22T11:17:42.000123+04:00
# output = 22-03-2024 11:17:42 +4
print(formated_date,time_part, timezone_part)
