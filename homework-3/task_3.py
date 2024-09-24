from datetime import date
from calendar import day_name

"""
დაწერეთ პროგრამა რომელიც მიიღებს 3 მნიშვნელობას: 
რომელ წელსაა დაბადებული ადამიანი, მერამდენე თვეშია დაბადებული და რა რიცხვშია დაბადებული. Შემდეგ კი ეკრანზე გამოიტანს კვირის რომელ დღესაა დაბადებული ადამიანი. 
იხ module datetime
"""

birth_year = int(input("Please enter your birthyear : "))
birth_month = int(input("Please enter your birth month : "))
birth_date = int(input("Please enter your birth date :"))

weekday_in_num = date(birth_year, birth_month, birth_date).weekday()
weekday_name = day_name[weekday_in_num]
print(f"You were born on a {weekday_name}")

